# Generated by Django 5.2 on 2025-06-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_orderticket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderticket',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
