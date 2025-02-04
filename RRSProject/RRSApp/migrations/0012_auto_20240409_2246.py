# Generated by Django 3.0 on 2024-04-09 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0011_auto_20240408_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='weekly', max_length=10),
        ),
        migrations.AddField(
            model_name='train',
            name='weekdays',
            field=models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rform',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RRSApp.Train'),
        ),
    ]
