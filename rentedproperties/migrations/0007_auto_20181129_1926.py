# Generated by Django 2.0.8 on 2018-11-29 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentedproperties', '0006_auto_20181129_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.Profile'),
        ),
    ]
