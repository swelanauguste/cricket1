# Generated by Django 3.2 on 2021-04-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210423_1741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BowlingStyle',
            new_name='Role',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='batting_style',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bowling_style',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ManyToManyField(to='users.Role'),
        ),
        migrations.DeleteModel(
            name='BattingStyle',
        ),
    ]