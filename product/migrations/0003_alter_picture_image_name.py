# Generated by Django 4.0.1 on 2022-01-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_picture_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image_name',
            field=models.CharField(blank=True, default='No picture', max_length=50),
        ),
    ]
