# Generated by Django 5.0.1 on 2024-02-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_service_ordering_alter_service_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmonial',
            old_name='authon',
            new_name='author',
        ),
    ]
