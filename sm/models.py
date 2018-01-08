from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    level = models.IntegerField()

class Procesados(models.Model):
    tipo_interaccion = models.CharField(max_length=80, null=True, blank=True)
    idioma = models.CharField(max_length=80, null=True, blank=True)
    polaridad = models.CharField(max_length=100, null=True, blank=True)
    anyo = models.IntegerField(null=True, blank=True)
    mes_nom = models.CharField(max_length=45, null=True, blank=True)
    mes_num = models.IntegerField(null=True, blank=True)
    dia_num = models.IntegerField(null=True, blank=True)
    dia_sem = models.CharField(max_length=45, null=True, blank=True)
    hora = models.IntegerField(null=True, blank=True)
    minuto = models.IntegerField(null=True, blank=True)
    isla = models.CharField(max_length=300, null=True, blank=True)
    municipio = models.CharField(max_length=300, null=True, blank=True)
    T_mallorca = models.IntegerField(null=True, blank=True)
    T_menorca = models.IntegerField(null=True, blank=True)
    T_ibiza = models.IntegerField(null=True, blank=True)
    T_formentera = models.IntegerField(null=True, blank=True)
    T_cine = models.IntegerField(null=True, blank=True)
    T_playa = models.IntegerField(null=True, blank=True)
    T_baile = models.IntegerField(null=True, blank=True)
    T_teatro = models.IntegerField(null=True, blank=True)
    T_arte = models.IntegerField(null=True, blank=True)
    T_musica = models.IntegerField(null=True, blank=True)
    T_conciertos = models.IntegerField(null=True, blank=True)
    T_restaurantes = models.IntegerField(null=True, blank=True)
    T_baleares = models.IntegerField(null=True, blank=True)
    T_hotel = models.IntegerField(null=True, blank=True)

class Tendencias(models.Model):
    nom_tendencia = models.CharField(max_length=150)
    total_ocurrencias = models.IntegerField(null=True, blank=True)
