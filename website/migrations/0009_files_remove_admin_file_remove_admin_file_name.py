# Generated by Django 4.0.4 on 2022-08-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_admin_file_admin_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='file',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='file_name',
        ),
    ]