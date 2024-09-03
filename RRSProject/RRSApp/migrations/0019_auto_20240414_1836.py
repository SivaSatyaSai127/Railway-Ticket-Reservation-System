# Generated by Django 3.0 on 2024-04-14 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0018_auto_20240414_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='ticket_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rform',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RRSApp.Train'),
        ),
    ]
