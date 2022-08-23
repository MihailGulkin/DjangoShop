# Generated by Django 4.1 on 2022-08-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('notebook', 'notebook'), ('accessories', 'accessories'), ('pc', 'pc'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]
