# Generated by Django 3.0.6 on 2020-06-08 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200608_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='tituto',
            new_name='titulo',
        ),
    ]
