# Generated by Django 3.2.5 on 2024-04-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0025_alter_story_writername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='writername',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
