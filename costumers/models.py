from django.db import models
from django.contrib.auth.models import User

class Costumer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='costumers',
        verbose_name='Usuário',
    )


