# Generated by Django 3.2 on 2021-05-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20210529_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
