# Generated by Django 4.0.4 on 2023-06-20 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_solicitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='rutSolcitante',
            new_name='rutSolicitante',
        ),
    ]
