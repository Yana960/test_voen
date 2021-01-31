from django.db import models

# Create your models here.
class VeloMarsh(models.Model):
	marsh_image = models.FileField(upload_to='images/')
	marsh_text = models.CharField(max_length=300)

class Quetion(models.Model):
	que_text = models.CharField(max_length=300)
	que_text_raz = models.CharField(max_length=300)