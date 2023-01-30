# Generated by Django 3.0.5 on 2020-06-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200624_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(upload_to='items/'),
        ),
    ]