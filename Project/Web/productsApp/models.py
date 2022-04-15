from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('Child', 'Child'),
        ('Nature', 'Nature'),
        ('People with disabilities', 'People with disabilities'),
        ('Covid','Covid')
    )
    title = models.CharField(max_length=50, verbose_name=' Theme title')
    description = models.TextField(verbose_name='Theme description')
    productType = models.CharField(choices=PRODUCTS_CHOICES,
                                   max_length=50,
                                   verbose_name='Theme type')
    # price = models.DecimalField(max_digits=7,
    #                             decimal_places=1,
    #                             blank=True,
    #                             null=True,
    #                             verbose_name='')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='Release')
    views = models.PositiveIntegerField('views', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Theme'
        ordering = ('-publishDate', )


class ProductImg(models.Model):
    product = models.ForeignKey(Product,
                                related_name='productImgs',
                                verbose_name='Theme',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Product/',
                              blank=True,
                              verbose_name='Theme photo')

    class Meta:
        verbose_name = 'Theme photo'
        verbose_name_plural = 'Theme photo'