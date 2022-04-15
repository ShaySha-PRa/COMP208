from django.db import models


# Create your models here.
class Award(models.Model):  # Model
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='description')
    photo = models.ImageField(upload_to='Award/',
                              blank=True,
                              verbose_name='Photo')

    class Meta:
        verbose_name = 'Award and honor'
        verbose_name_plural = 'Award and honor'
