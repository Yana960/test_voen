# Generated by Django 3.1.5 on 2021-01-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VeloMarsh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marsh_image', models.ImageField(upload_to='marsh_images/')),
                ('marsh_text', models.CharField(max_length=300)),
            ],
        ),
    ]
