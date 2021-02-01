# Generated by Django 3.1.5 on 2021-01-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeloArticlesZagl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articlez_image', models.FileField(upload_to='images/')),
                ('articlez_text', models.TextField()),
                ('articlez_heading', models.CharField(max_length=300)),
                ('articlez_date', models.DateTimeField()),
            ],
        ),
    ]