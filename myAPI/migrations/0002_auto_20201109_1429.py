# Generated by Django 3.1.3 on 2020-11-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_barang', models.CharField(max_length=100)),
                ('harga_barang', models.FloatField()),
                ('stock_barang', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
