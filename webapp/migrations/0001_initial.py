# Generated by Django 3.2 on 2021-04-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('telegram_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('facebok_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
