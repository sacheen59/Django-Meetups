# Generated by Django 5.0.6 on 2024-06-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_meetups_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetups',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
