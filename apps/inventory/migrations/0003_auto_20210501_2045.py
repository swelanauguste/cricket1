# Generated by Django 3.2 on 2021-05-02 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210501_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='assets_holder',
        ),
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]