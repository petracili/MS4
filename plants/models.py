from django.db import models

# Create your models here.
class Plants(models.Model):

    class Meta:
        verbose_name_plural = 'Plants'

    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name