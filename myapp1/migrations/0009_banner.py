# Generated by Django 5.0.1 on 2024-02-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0008_rename_protfolio_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bannerImage/')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
