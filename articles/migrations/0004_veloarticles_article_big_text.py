# Generated by Django 3.1.5 on 2021-01-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_delete_veloarticleszagl'),
    ]

    operations = [
        migrations.AddField(
            model_name='veloarticles',
            name='article_big_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
