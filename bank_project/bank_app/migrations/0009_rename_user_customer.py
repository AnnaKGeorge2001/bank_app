# Generated by Django 4.2.5 on 2023-11-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0008_material_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
