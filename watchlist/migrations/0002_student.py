# Generated by Django 5.1.4 on 2025-01-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]