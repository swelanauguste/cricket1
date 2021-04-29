# Generated by Django 3.2 on 2021-04-21 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BattingStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('batting_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.battingstyle')),
                ('bowling_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.bowlingstyle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.PositiveIntegerField(default=0)),
                ('innings', models.PositiveIntegerField(default=0)),
                ('balls', models.PositiveIntegerField(default=0, verbose_name='not out')),
                ('runs', models.PositiveBigIntegerField(default=0)),
                ('wkts', models.PositiveIntegerField(default=0, verbose_name='wickets')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BattingProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.PositiveIntegerField(default=0)),
                ('innings', models.PositiveIntegerField(default=0)),
                ('no', models.PositiveIntegerField(default=0, verbose_name='not out')),
                ('runs', models.PositiveBigIntegerField(default=0)),
                ('hs', models.PositiveIntegerField(default=0, verbose_name='highest score')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
