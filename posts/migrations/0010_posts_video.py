# Generated by Django 5.0.6 on 2024-07-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='video',
            field=models.FileField(default=2, upload_to='videos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]