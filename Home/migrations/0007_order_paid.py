# Generated by Django 4.0.3 on 2022-03-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
