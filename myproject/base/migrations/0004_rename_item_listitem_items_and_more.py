# Generated by Django 4.1.1 on 2022-10-03 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_name_listitem_named'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='item',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='listitem',
            old_name='named',
            new_name='title',
        ),
    ]