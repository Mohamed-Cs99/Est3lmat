# Generated by Django 5.0.1 on 2024-01-21 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0002_alter_person_approval'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='renk',
            new_name='rank',
        ),
    ]
