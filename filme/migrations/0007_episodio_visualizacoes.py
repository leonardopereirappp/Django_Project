# Generated by Django 4.1.2 on 2022-11-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0006_delete_subfilms'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='visualizacoes',
            field=models.IntegerField(default=0),
        ),
    ]
