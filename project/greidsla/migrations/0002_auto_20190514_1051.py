# Generated by Django 2.2.1 on 2019-05-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greidsla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('ssn', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=50)),
                ('house_num', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='city',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='country',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='house_num',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='ssn',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='zip',
        ),
    ]
