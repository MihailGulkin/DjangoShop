# Generated by Django 4.1 on 2022-08-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('mobile', 'mobile'), ('pc', 'pc'), ('notebook', 'notebook'), ('accessories', 'accessories')], default='mobile', max_length=20),
        ),
    ]