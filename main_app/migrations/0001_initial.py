# Generated by Django 4.1.2 on 2022-10-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capybara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
                ('image', models.TextField(max_length=500)),
            ],
        ),
    ]
