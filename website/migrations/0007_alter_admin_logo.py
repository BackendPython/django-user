# Generated by Django 4.0.4 on 2022-08-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_admin_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]
