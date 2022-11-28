from cities_light.models import City
from django.db import models

from users.models import UserProfile


class Post(models.Model):
    '''
    Модель для объявления.
    '''
    title = models.CharField(max_length=150, verbose_name='Название объявления')
    price = models.IntegerField(verbose_name='Цена')
    content = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    is_published = models.BooleanField(default=True, verbose_name='Статус объявления')
    location = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
    

class Category(models.Model):
    '''
    Модель категорий.
    '''
    main_category = models.CharField(max_length=100, verbose_name='Категория')
    sub_category = models.CharField(max_length=100, verbose_name='Подкатегория')

    def __str__(self) -> str:
        '''
        Возвращаем в формате <Автомобили: Запчасти>.
        '''
        return self.main_category + ': ' + self.sub_category
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Tag(models.Model):
    '''
    Модель тэгов. Для каждой категории используются свои теги.
    '''
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    
    def __str__(self) -> str:
        return self.name + ' (' + str(self.category) + ')'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    
    def __str__(self) -> str:
        return self.image.name
