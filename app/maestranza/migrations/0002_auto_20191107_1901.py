# Generated by Django 2.2.3 on 2019-11-07 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestranza', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Encargado',
            new_name='Persona',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='nombre_encargado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='encargado',
            new_name='persona',
        ),
    ]
