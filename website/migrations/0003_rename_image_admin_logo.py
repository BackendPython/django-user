# Generated by Django 4.0.4 on 2022-07-22 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_admin_image_alter_admin_email_alter_admin_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='image',
            new_name='logo',
        ),
    ]
