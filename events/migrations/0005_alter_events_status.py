# Generated by Django 5.1.6 on 2025-04-23 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('expired', 'Expired')], default='active', max_length=8),
        ),
    ]
