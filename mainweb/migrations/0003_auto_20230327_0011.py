# Generated by Django 3.2 on 2023-03-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0002_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='our_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company'),
        ),
    ]