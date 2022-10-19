# Generated by Django 4.1.1 on 2022-10-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_serre_culture_remove_serre_person_delete_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serre',
            name='kult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serrekult', to='base.culture'),
        ),
        migrations.AddField(
            model_name='serre',
            name='pers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serrepers', to='base.person'),
        ),
    ]
