# Generated by Django 4.1.5 on 2023-03-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_stock_security_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='longitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]