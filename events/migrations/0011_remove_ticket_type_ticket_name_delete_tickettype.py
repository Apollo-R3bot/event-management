# Generated by Django 5.1.6 on 2025-04-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_orderticket_qty_orderticket_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='type',
        ),
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.CharField(default='Free', max_length=100),
        ),
        migrations.DeleteModel(
            name='TicketType',
        ),
    ]
