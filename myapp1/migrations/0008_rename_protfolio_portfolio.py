# Generated by Django 5.0.1 on 2024-02-18 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0007_protfolio_remove_contact_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Protfolio',
            new_name='Portfolio',
        ),
    ]
