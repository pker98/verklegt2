# Generated by Django 2.2.1 on 2019-05-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasteignasala', '0002_auto_20190509_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='town',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartment',
            name='zip',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]