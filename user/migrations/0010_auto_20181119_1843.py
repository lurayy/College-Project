# Generated by Django 2.1 on 2018-11-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20181119_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='current_semester',
            new_name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
