# Generated by Django 5.2 on 2025-04-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_project_options_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
