from django.db import models

# Create your models here.
class VeloMarsh(models.Model):
	marsh_image = models.FileField(upload_to='images/')
	marsh_text = models.CharField(max_length=300)