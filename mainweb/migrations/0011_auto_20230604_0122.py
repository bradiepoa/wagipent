# Generated by Django 3.2 on 2023-06-03 22:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0010_currentandpreviousevents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdescription',
            options={'verbose_name_plural': '05. why work with us'},
        ),
        migrations.AlterModelOptions(
            name='currentandpreviousevents',
            options={'verbose_name_plural': '21. Current And Previous Events'},
        ),
        migrations.AlterField(
            model_name='contactdescription',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
