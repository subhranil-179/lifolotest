# Generated by Django 4.1.3 on 2022-12-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_article_keywords_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='canonical',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/articles/2022/12/17'),
        ),
    ]
