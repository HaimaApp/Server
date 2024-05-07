# Generated by Django 5.0.4 on 2024-05-07 17:48

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Ab', 'Abaya'), ('Ji', 'Jilbaab'), ('Niq', 'Niqab'), ('Hi', 'Hijaab'), ('Dr', 'Dress')], default=None, max_length=20)),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(choices=[('SM', 'SMALL'), ('MED', 'MEDIUM'), ('LRG', 'LARGE')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.PositiveIntegerField(default=0)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='images/')),
                ('in_stock', models.BooleanField(default=True)),
                ('by_protect_fee', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.sizevariant')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productmodel')),
            ],
        ),
    ]
