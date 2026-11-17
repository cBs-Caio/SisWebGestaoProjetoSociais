from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField("descrição", blank=True)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "inscrição"
        verbose_name_plural = "inscrições"
        constraints = [
            models.UniqueConstraint(
                fields=["participante", "curso"],
                name="gestao_inscricao_participante_curso_unica",
                violation_error_message="Este participante já está inscrito neste curso.",
            ),
        ]

    def __str__(self):
        return f"{self.participante} — {self.curso}"


class Frequencia(models.Model):
    inscricao = models.ForeignKey(
        Inscricao, on_delete=models.PROTECT, verbose_name="inscrição"
    )
    data = models.DateField()
    presente = models.BooleanField(default=False)

    class Meta:
        verbose_name = "frequência"
        verbose_name_plural = "frequências"
        constraints = [
            models.UniqueConstraint(
                fields=["inscricao", "data"],
                name="gestao_frequencia_inscricao_data_unica",
                violation_error_message="Já existe uma frequência para esta inscrição nesta data.",
            ),
        ]

    def __str__(self):
        return f"{self.inscricao} ({self.data:%d/%m/%Y})"
