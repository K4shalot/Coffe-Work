# Generated by Django 5.2 on 2025-04-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wificafe', '0002_cafeblock_full_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeblock',
            name='google_map_embed',
            field=models.TextField(blank=True, null=True),
        ),
    ]
