# Generated by Django 3.2.8 on 2021-10-29 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor.vendor'),
        ),
    ]
