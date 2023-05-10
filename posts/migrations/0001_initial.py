# Generated by Django 4.2.1 on 2023-05-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
