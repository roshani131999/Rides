# Generated by Django 2.2.2 on 2020-02-17 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200214_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverbooking',
            name='DBFrom',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driverbooking',
            name='DBTo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driverbooking',
            name='Did',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='homepage.DriverData'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBIscancel',
            field=models.CharField(default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBisconform',
            field=models.CharField(default='no', max_length=5),
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBisdelete',
            field=models.CharField(default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBmessage',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBnotes',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='driverbooking',
            name='DBreasonforcancel',
            field=models.CharField(default='', max_length=50),
        ),
    ]
