# Generated by Django 4.1.3 on 2022-11-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things_backend', '0005_rename_post_id_photo_post_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='<property object at 0x7f940eaf28e0>/<property object at 0x7f940eaf22f0>/'),
        ),
    ]