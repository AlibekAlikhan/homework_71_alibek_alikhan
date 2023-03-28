# Generated by Django 4.1.6 on 2023-03-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.IntegerField(default=0, verbose_name='Количество Комментариев'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Количество Лайков'),
        ),
    ]
