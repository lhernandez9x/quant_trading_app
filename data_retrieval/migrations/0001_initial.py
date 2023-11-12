# Generated by Django 4.2.7 on 2023-11-12 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'symbol',
            },
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('volume', models.IntegerField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_retrieval.symbol')),
            ],
            options={
                'verbose_name_plural': 'prices',
            },
        ),
    ]
