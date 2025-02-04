# Generated by Django 3.0 on 2024-04-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0008_rform_train'),
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
            name='noft',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rform',
            name='pno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='rform',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RRSApp.Train'),
        ),
    ]
