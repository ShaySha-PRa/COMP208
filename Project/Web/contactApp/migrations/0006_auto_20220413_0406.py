# Generated by Django 2.2.4 on 2022-04-12 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0005_auto_20220408_0340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('-publishDate',), 'verbose_name': 'ADs', 'verbose_name_plural': 'ADs'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ('-status', '-publishDate'), 'verbose_name': 'Resume', 'verbose_name_plural': 'Resume'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(verbose_name='Position required'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='publishDate',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='update date'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Recruiting Position'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2022-04-13', max_length=20, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='photo',
            field=models.ImageField(upload_to='contact/recruit/%Y_%m_%d', verbose_name='personal photo'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='publishDate',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='Update time'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.IntegerField(choices=[(1, 'quering'), (2, 'Passed'), (3, 'Not passed')], default=1, verbose_name='Interview result'),
        ),
    ]
