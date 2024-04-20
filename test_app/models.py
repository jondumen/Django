from django.db import models

# Create your models here.
class uwu(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    mail = models.EmailField(unique=True)
    tel = models.CharField(max_length=15)

    def __str__(self):
        return self.mail