# Generated by Django 5.0.1 on 2024-02-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0010_testmonial_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newfeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
