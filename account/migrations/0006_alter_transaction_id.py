# Generated by Django 3.2.3 on 2021-05-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210527_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
