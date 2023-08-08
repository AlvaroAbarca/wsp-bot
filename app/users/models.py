from django.db import models

from datetime import datetime

# Create your models here.
class Person(models.Model):

    name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30, blank=True, null=True)
    birthday = models.DateField("Fecha Nacimiento", default=datetime.now, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.last_name} - {self.birthday}"