# Generated by Django 2.1.2 on 2018-10-16 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181016_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
