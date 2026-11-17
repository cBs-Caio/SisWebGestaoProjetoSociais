from django.contrib import admin

from .models import Curso, Frequencia, Inscricao, Participante


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    search_fields = ("nome",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ("nome",)


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ("participante", "curso", "criada_em")
    list_filter = ("curso",)
    search_fields = ("participante__nome", "curso__nome")
    autocomplete_fields = ("participante", "curso")


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ("inscricao", "data", "presente")
    list_filter = ("presente", "data")
    search_fields = ("inscricao__participante__nome", "inscricao__curso__nome")
    autocomplete_fields = ("inscricao",)
    list_select_related = ("inscricao__participante", "inscricao__curso")
