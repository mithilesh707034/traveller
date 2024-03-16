# Generated by Django 3.2.20 on 2024-03-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20240315_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('otp', models.IntegerField(default=-115151)),
            ],
        ),
    ]