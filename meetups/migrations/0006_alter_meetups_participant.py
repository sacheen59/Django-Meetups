# Generated by Django 5.0.6 on 2024-06-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_participant_meetups_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetups',
            name='participant',
            field=models.ManyToManyField(blank=True, to='meetups.participant'),
        ),
    ]
