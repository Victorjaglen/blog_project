# Generated by Django 5.1.3 on 2024-11-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
