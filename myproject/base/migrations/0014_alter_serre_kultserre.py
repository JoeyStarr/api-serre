# Generated by Django 4.1.1 on 2022-10-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_serre_kultserre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serre',
            name='kultSerre',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
