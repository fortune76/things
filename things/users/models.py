from cities_light.models import City
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    '''
    Модель для профилей пользователей.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=60, verbose_name='Имя', null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='Город', null=True)
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    phone = PhoneNumberField(blank=False, unique=True, verbose_name='Номер телефона', null=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars', null=True)
    
    def __str__(self) -> str:
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender: User, instance: User, created: bool, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, name=instance.username)
    