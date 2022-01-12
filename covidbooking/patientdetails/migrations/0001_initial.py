# Generated by Django 3.2.5 on 2022-01-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('firstdose', models.BooleanField()),
                ('seconddose', models.BooleanField()),
            ],
        ),
    ]
