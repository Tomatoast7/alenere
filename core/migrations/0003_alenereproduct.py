# Generated by Django 5.1.4 on 2024-12-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='alenereproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]