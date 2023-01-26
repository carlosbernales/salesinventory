# Generated by Django 4.1.4 on 2023-01-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=255)),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('caty_name', models.CharField(max_length=100)),
                ('s_product', models.CharField(max_length=100)),
                ('s_price', models.CharField(max_length=255)),
                ('s_quantity', models.CharField(max_length=255)),
                ('s_total', models.CharField(max_length=255)),
            ],
        ),
    ]
