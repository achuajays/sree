# Generated by Django 4.1.5 on 2023-05-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='s_name',
            field=models.CharField(default='  ', max_length=100),
        ),
    ]