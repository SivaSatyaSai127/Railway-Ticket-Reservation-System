# Generated by Django 3.2.5 on 2024-04-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRSApp', '0024_story_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='writername',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
