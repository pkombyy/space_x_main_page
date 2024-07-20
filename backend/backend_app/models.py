from django.db import models

#модель блоков меню
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.title
    
#модель блоков преимуществ
class FeatureBlock(models.Model):
    description=models.TextField(max_length=40)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Feature Block'
        verbose_name_plural = 'Feature Blocks'

    def __str__(self):
        return self.description

