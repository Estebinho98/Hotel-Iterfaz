# Generated by Django 5.1.1 on 2024-10-07 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Marriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name_spouse1', models.CharField(max_length=200)),
                ('Full_name_spouse2', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('exit_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.rooms')),
                ('services', models.ManyToManyField(to='Reservas.services')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('members', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('exit_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.rooms')),
                ('services', models.ManyToManyField(to='Reservas.services')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('exit_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservas.rooms')),
                ('services', models.ManyToManyField(to='Reservas.services')),
            ],
        ),
    ]
