# Generated by Django 3.2 on 2021-05-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210501_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='count',
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True, verbose_name='details'),
        ),
    ]