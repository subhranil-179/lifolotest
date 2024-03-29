# Generated by Django 4.1.3 on 2022-12-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/articles/2022/12/16'),
        ),
    ]
