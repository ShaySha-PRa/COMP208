from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Doc(models.Model):
    title = models.CharField(max_length=250, verbose_name='Data name')
    file = models.FileField(upload_to='Service/',
                            blank=True,
                            verbose_name='File data')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='Release')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "Data"
        verbose_name_plural = verbose_name