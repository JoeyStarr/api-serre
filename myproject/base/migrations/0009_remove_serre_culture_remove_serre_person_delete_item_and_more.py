# Generated by Django 4.1.1 on 2022-10-05 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_culture_person_serre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serre',
            name='culture',
        ),
        migrations.RemoveField(
            model_name='serre',
            name='person',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Listitem',
        ),
    ]
