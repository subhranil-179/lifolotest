# Generated by Django 4.1.3 on 2022-12-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/articles/2022/12/15'),
        ),
    ]
