from django.db import models

# Create your models here.
class VeloMarsh(models.Model):
	marsh_image = models.FileField(upload_to='images/')
	marsh_text = models.CharField(max_length=300)

class HistoryMarsh(models.Model):
	history_marsh_name = models.CharField(max_length=100)
	history_marsh_image = models.FileField(upload_to='images/')
	history_marsh_text = models.TextField()
	history_marsh_km = models.CharField(max_length=300)
	history_marsh_time = models.CharField(max_length=30)
	history_marsh_obj = models.CharField(max_length=300)

class WarMarsh(models.Model):
	war_marsh_name = models.CharField(max_length=100)
	war_marsh_image = models.FileField(upload_to='images/')
	war_marsh_text = models.TextField()
	war_marsh_km = models.CharField(max_length=300)
	war_marsh_time = models.CharField(max_length=30)
	war_marsh_obj = models.CharField(max_length=300)
