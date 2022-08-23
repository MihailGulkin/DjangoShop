# Generated by Django 4.1 on 2022-08-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('accessories', 'accessories'), ('pc', 'pc'), ('notebook', 'notebook'), ('mobile', 'mobile')], default='mobile', max_length=20),
        ),
    ]
