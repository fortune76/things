# Generated by Django 4.1.3 on 2022-11-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things_backend', '0003_alter_photo_image_alter_post_image_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_id',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='<property object at 0x7efe5dbe2980>/<property object at 0x7efe5dbe2390>/'),
        ),
    ]