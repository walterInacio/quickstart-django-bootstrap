from django.db import models

class Esportes(models.Model):

    CHOICES = (
        ('M','Masculino'),
        ('F','Feminino'),
    )

    modalidade = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    tipo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    distancia = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    sexo = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=CHOICES
    )

    local = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'esportes'

    def __str__(self):
        return self.modalidade
