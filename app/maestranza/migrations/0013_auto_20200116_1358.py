# Generated by Django 2.2.3 on 2020-01-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maestranza', '0012_auto_20200116_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='estado',
        ),
        migrations.AddField(
            model_name='estado',
            name='detalles',
            field=models.CharField(default='diseno', max_length=1000),
        ),
    ]
