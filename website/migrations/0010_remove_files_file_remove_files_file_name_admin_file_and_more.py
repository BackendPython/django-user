# Generated by Django 4.0.4 on 2022-08-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_files_remove_admin_file_remove_admin_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file',
        ),
        migrations.RemoveField(
            model_name='files',
            name='file_name',
        ),
        migrations.AddField(
            model_name='admin',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='file_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]