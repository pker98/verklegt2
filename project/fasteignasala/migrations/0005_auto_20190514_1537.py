# Generated by Django 2.2.1 on 2019-05-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasteignasala', '0004_auto_20190514_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='estimated_value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='fire_insurance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='num_bath_room',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='num_bed_room',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='num_rooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
