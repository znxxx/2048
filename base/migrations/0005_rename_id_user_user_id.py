# Generated by Django 4.2.5 on 2023-09-14 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_detail_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]
