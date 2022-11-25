from django.contrib.auth.models import User
from django.db import models
from cities_light.models import City
from phonenumber_field.modelfields import PhoneNumberField

from things.things_backend.models import Post

class UserProfile(models.Model):
    '''
    Кастомное поле города, чтобы город можно было выбрать только из существующих.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=60, verbose_name='Имя')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='Город')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Номер телефона')
    avatar = models.ImageField(verbose_name='Аватар')
    posts = models.ManyToOneRel(Post, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.name
    
    