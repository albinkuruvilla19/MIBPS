# Generated by Django 5.0.6 on 2024-07-13 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_alter_management_principal_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsnevents',
            name='content1',
        ),
        migrations.RemoveField(
            model_name='newsnevents',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='newsnevents',
            name='image',
        ),
    ]