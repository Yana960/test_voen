# Generated by Django 3.1.5 on 2021-02-03 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0012_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historymarsh',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='velo.velomarsh', verbose_name='Категория'),
        ),
    ]
