# Generated by Django 4.1.2 on 2022-10-19 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='cleaning date'),
        ),
    ]
