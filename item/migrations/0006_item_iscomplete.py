# Generated by Django 2.2.1 on 2019-06-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20190602_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='isComplete',
            field=models.BooleanField(default=0),
        ),
    ]
