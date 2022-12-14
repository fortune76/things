# Generated by Django 4.1.3 on 2022-11-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(max_length=100, verbose_name='Категория')),
                ('sub_category', models.CharField(max_length=100, verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='<property object at 0x7f4fda94a700>/<property object at 0x7f4fda94a160>/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things_backend.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название объявления')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус объявления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='things_backend.category', verbose_name='Категория')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things_backend.photo', verbose_name='Фото')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cities_light.city', verbose_name='Город')),
                ('tags', models.ManyToManyField(to='things_backend.tag', verbose_name='Теги')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things_backend.post'),
        ),
    ]
