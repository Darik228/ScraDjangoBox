# Generated by Django 5.0.2 on 2024-03-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeddata',
            name='image_url',
            field=models.URLField(max_length=255),
        ),
    ]