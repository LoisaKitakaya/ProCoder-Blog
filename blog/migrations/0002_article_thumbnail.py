# Generated by Django 3.2.11 on 2022-01-12 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='thumbnails/'),
            preserve_default=False,
        ),
    ]
