# Generated by Django 3.2.9 on 2021-12-09 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('self_report', '0004_alter_attitudemodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilityModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('ability_01_01', models.CharField(max_length=200)),
                ('ability_01_02', models.CharField(max_length=200)),
                ('ability_02_01', models.CharField(max_length=200)),
                ('ability_03_01', models.CharField(max_length=200)),
                ('ability_03_02', models.CharField(max_length=200)),
                ('ability_03_03', models.CharField(max_length=200)),
                ('ability_04_01', models.CharField(max_length=200)),
                ('ability_04_02', models.CharField(max_length=200)),
                ('ability_05_01', models.CharField(max_length=200)),
                ('ability_05_02', models.CharField(max_length=200)),
                ('ability_06_01', models.CharField(max_length=200)),
                ('ability_06_02', models.CharField(max_length=200)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='foreign_key')),
            ],
        ),
    ]
