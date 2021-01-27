from django.db import models

# Create your models here.
class VeloObject(models.Model):
	object_image = models.FileField(upload_to='images/')
	object_image_map = models.FileField(upload_to='images/')
	object_text = models.TextField()
	object_heading = models.CharField(max_length=300)