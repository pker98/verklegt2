# Generated by Django 2.2.1 on 2019-05-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=20)),
                ('fire_insurance', models.CharField(max_length=20)),
                ('estimated_value', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('num_rooms', models.CharField(max_length=2)),
                ('num_bed_room', models.CharField(max_length=2)),
                ('num_bath_room', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fasteignasala.Apartment')),
            ],
        ),
    ]
