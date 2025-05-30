# Generated by Django 5.1 on 2025-05-22 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='product_title_snapshot',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_history', to='base.trackedproduct'),
        ),
    ]
