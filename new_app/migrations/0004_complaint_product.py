# Generated by Django 5.0.4 on 2024-11-24 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_jobapplication_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_app.product'),
        ),
    ]
