# Generated by Django 3.2.23 on 2023-11-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='My default description'),
            preserve_default=False,
        ),
    ]
