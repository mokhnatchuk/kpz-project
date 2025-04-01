from django.db import models

class Category(models.Model):
    category = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField('Слаг', unique=True, help_text='Automatically generated slug')  # New field

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category
