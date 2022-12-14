# Generated by Django 4.1.2 on 2022-11-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0004_alter_episodio_num_ep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subfilms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_subfilms', models.CharField(choices=[('Excel Impressionador', 'EXCEL IMPRESSIONADOR'), ('Power B.I. Impressionador', 'POWER B.I. IMPRESSIONADOR'), ('Python Impressionador', 'PYTHON IMPRESSIONADOR')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='episodio',
            name='num_ep',
            field=models.IntegerField(default=0),
        ),
    ]
