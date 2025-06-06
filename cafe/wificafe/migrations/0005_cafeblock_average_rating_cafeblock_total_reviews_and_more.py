# Generated by Django 5.2 on 2025-04-07 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wificafe', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeblock',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cafeblock',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CafePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cafe_photos/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='wificafe.cafeblock')),
            ],
        ),
    ]
