# Generated by Django 4.1.6 on 2023-03-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='photo',
            field=models.ImageField(default='default_child_photo.jpg', upload_to='child_photos'),
        ),
    ]
