# Generated by Django 2.2.2 on 2020-02-12 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarUser',
            fields=[
                ('CUID', models.AutoField(primary_key=True, serialize=False)),
                ('CUisac', models.CharField(max_length=50)),
                ('CUminfair', models.CharField(max_length=10)),
                ('CUacfair', models.CharField(default=50, max_length=10)),
                ('CUnotes', models.CharField(max_length=50)),
                ('CUIsdriver', models.CharField(max_length=50)),
                ('CarImage', models.CharField(max_length=20)),
                ('CCID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='homepage.CarCompany')),
                ('Uid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='homepage.UserData')),
            ],
        ),
    ]
