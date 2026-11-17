from datetime import date

from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from .models import Curso, Frequencia, Inscricao, Participante


class RegistroSocialTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.participante = Participante.objects.create(nome="Ana Exemplo")
        cls.curso = Curso.objects.create(nome="Informática")
        cls.inscricao = Inscricao.objects.create(
            participante=cls.participante, curso=cls.curso
        )

    def test_inscricao_duplicada_tem_mensagem_de_validacao(self):
        duplicada = Inscricao(participante=self.participante, curso=self.curso)
        with self.assertRaisesMessage(ValidationError, "já está inscrito neste curso"):
            duplicada.full_clean()

    def test_banco_rejeita_inscricao_duplicada(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Inscricao.objects.create(participante=self.participante, curso=self.curso)

    def test_participante_pode_se_inscrever_em_outro_curso(self):
        outro_curso = Curso.objects.create(nome="Leitura")
        Inscricao.objects.create(participante=self.participante, curso=outro_curso)
        self.assertEqual(self.participante.inscricao_set.count(), 2)

    def test_banco_admite_chamadas_em_dias_distintos(self):
        Frequencia.objects.create(
            inscricao=self.inscricao, data=date(2026, 1, 10), presente=True
        )
        Frequencia.objects.create(inscricao=self.inscricao, data=date(2026, 1, 11))
        self.assertEqual(self.inscricao.frequencia_set.count(), 2)

    def test_banco_rejeita_frequencia_duplicada_no_mesmo_dia(self):
        dia = date(2026, 1, 10)
        Frequencia.objects.create(inscricao=self.inscricao, data=dia, presente=True)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Frequencia.objects.create(inscricao=self.inscricao, data=dia)

    def test_exclusao_de_participante_com_inscricao_e_bloqueada(self):
        with self.assertRaises(ProtectedError):
            self.participante.delete()

    def test_exclusao_de_inscricao_com_frequencia_e_bloqueada(self):
        Frequencia.objects.create(inscricao=self.inscricao, data=date(2026, 1, 10))
        with self.assertRaises(ProtectedError):
            self.inscricao.delete()
