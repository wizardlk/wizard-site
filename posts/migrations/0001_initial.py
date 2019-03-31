# Generated by Django 2.1.7 on 2019-03-31 04:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(blank=True, default='', max_length=250)),
                ('full_description', models.TextField(blank=True, default='')),
                ('watch_link', models.CharField(default='', max_length=250, verbose_name='video watch url')),
                ('embed_link', models.CharField(default='', max_length=250, verbose_name='video embed url')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
    ]
