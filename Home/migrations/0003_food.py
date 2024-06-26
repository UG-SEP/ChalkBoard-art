# Generated by Django 4.0.3 on 2022-03-21 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_categories_delete_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('is_special', models.BooleanField()),
                ('is_popular', models.BooleanField()),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='media')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.categories')),
            ],
        ),
    ]
