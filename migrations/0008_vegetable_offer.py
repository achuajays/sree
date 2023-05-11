# Generated by Django 4.1.5 on 2023-05-11 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_loc_order_s_loc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_offered', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity_offered', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vegetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vegetable')),
            ],
        ),
    ]
