# Generated by Django 4.1.5 on 2023-05-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_log_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='s_loc',
            field=models.CharField(default='trivandrum', max_length=100),
        ),
        migrations.AddField(
            model_name='shop',
            name='s_loc',
            field=models.CharField(default='trivandrum', max_length=100),
        ),
    ]
