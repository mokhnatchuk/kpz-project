from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField('Слаг', unique=True, help_text='Automatically generated slug')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return f"/articles/category/{self.slug}"

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 сим.')
    description = models.TextField(blank=True, verbose_name='Опис')
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    slug = models.SlugField('Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField('Головна', default=True, help_text='Показувати на головній сторінці')
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True, verbose_name='Категорія', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/articles/{self.pub_date.strftime('%Y')}/{self.pub_date.strftime('%m')}/{self.pub_date.strftime('%d')}/{self.slug}"

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name='Стаття', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='photos')
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 сим.', blank=True)

    class Meta:
        verbose_name = 'Фото для статті'
        verbose_name_plural = 'Фото для статті'

    def __str__(self):
        return self.title
