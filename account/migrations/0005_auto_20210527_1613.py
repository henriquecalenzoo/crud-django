# Generated by Django 3.2.3 on 2021-05-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
