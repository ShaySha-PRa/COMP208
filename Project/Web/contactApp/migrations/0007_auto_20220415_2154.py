# Generated by Django 2.2.4 on 2022-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0006_auto_20220413_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2022-04-15', max_length=20, verbose_name='date of birth'),
        ),
    ]
