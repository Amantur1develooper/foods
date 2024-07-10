from django.db import models

# Create your models here.
class Foods(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя продукта')
    price = models.IntegerField(verbose_name='цена')
    image = models.ImageField(upload_to='image_product', null=True, blank=True )
    count = models.IntegerField(verbose_name='количество')
    
    
    