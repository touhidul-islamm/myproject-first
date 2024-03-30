# Generated by Django 5.0.1 on 2024-02-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=12)),
                ('web', models.URLField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testmonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authon', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Working_hour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('mon_wed', models.CharField(max_length=50)),
                ('thus_fri', models.CharField(max_length=50)),
                ('saturday', models.CharField(max_length=50)),
                ('sunday', models.CharField(max_length=50)),
            ],
        ),
    ]