# Generated by Django 5.0.6 on 2024-06-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_category_slug_alter_posts_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.TextField(),
        ),
    ]