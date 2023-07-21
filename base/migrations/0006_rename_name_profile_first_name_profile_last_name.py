# Generated by Django 4.2.3 on 2023-07-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_message_options_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]