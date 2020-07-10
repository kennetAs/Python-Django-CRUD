from django.db import models

# Create your models here.

class Employee(models.Model):
    fuulname = models.CharField(max_length = 100)
    cpf = models.IntegerField()
    profession = models.CharField(max_length = 100)
    salary = models.IntegerField()

    def __str__(self):
        return self.profession
