# Generated by Django 2.2.3 on 2020-01-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestranza', '0005_persona_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Asignado'), (1, 'trabajando'), (2, 'terminado')], default=0),
        ),
    ]
