# Generated by Django 3.0 on 2024-04-14 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0017_auto_20240409_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='train',
            name='weekdays',
        ),
        migrations.AlterField(
            model_name='rform',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RRSApp.Train'),
        ),
    ]
