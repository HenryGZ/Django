# Generated by Django 5.0.1 on 2024-01-21 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
