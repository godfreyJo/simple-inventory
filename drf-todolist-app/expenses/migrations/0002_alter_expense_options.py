# Generated by Django 4.0.6 on 2022-09-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-updated_at']},
        ),
    ]