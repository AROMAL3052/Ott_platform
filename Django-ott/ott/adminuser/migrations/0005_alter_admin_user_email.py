# Generated by Django 5.0.7 on 2024-10-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminuser', '0004_rename_adminuser_admin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_user',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
