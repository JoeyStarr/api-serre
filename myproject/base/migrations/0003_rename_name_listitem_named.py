# Generated by Django 4.1.1 on 2022-10-03 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_listitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='name',
            new_name='named',
        ),
    ]
