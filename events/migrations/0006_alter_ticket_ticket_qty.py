# Generated by Django 5.1.6 on 2025-04-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_events_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_qty',
            field=models.IntegerField(default=1),
        ),
    ]
