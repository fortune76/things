# Generated by Django 4.1.3 on 2022-11-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things_backend', '0008_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='<django.db.models.fields.related.ForeignKey>/'),
        ),
    ]