# Generated by Django 2.1 on 2018-11-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_auto_20181124_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='mark',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
