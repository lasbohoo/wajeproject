# Generated by Django 3.2 on 2022-07-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assesment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
