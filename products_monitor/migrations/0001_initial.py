# Generated by Django 2.1.7 on 2019-03-19 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('SKU', models.CharField(max_length=200)),
                ('stock_status', models.BinaryField()),
                ('url', models.URLField()),
                ('picture_url', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('restock_date', models.DateTimeField(verbose_name='date restocked')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_monitor.Brand')),
            ],
        ),
    ]