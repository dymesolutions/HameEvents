# Generated by Django 2.2.9 on 2020-02-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0073_soft_delete_replaced_objects'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='accessible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='multi_day',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='pin',
            field=models.CharField(default='0000', max_length=64),
        ),
        migrations.AddField(
            model_name='event',
            name='provider_email',
            field=models.EmailField(blank=True, default='admin@tavastiaevents.fi', max_length=254, null=True),
        ),
    ]