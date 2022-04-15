from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.


class MyNew(models.Model):
    NEWS_CHOICES = (
        ('Organization progress', 'Organization progress'),
        ('Social news', 'Social news'),
        ('Public Release', 'Public Release'),
    )
    title = models.CharField(max_length=50, verbose_name=' News title')
    description = UEditorField(u'content',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='news/images/',
                               filePath='news/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='News type')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='Release time')
    views = models.PositiveIntegerField('views', default=0)
    photo = models.ImageField(upload_to='news/',
                              blank=True,
                              null=True,
                              verbose_name='Results figure')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "News"
        verbose_name_plural = verbose_name