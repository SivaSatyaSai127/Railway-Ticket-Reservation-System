# Generated by Django 3.0 on 2024-04-08 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0010_auto_20240408_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='arrtimedes',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='train',
            name='deptimesrc',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rform',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RRSApp.Train'),
        ),
    ]
