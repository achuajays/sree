# Generated by Django 4.1.5 on 2023-05-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_log_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=20)),
                ('policy_holder', models.CharField(max_length=100)),
                ('crop_insured', models.CharField(max_length=50)),
                ('acres_insured', models.FloatField()),
                ('premium_amount', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
