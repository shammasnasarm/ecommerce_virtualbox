# Generated by Django 3.2.4 on 2021-06-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
