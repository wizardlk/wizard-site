# Generated by Django 2.1.7 on 2019-03-26 15:39

from django.db import migrations, models


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
                ('short_description', models.CharField(max_length=250)),
                ('full_description', models.CharField(max_length=2500)),
                ('link', models.CharField(max_length=250)),
                ('published_at', models.DateTimeField(verbose_name='date published')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
