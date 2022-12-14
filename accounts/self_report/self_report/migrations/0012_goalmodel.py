# Generated by Django 3.2.9 on 2021-12-13 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('self_report', '0011_reportetcmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('team', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('goal_01_01', models.CharField(max_length=200, null=True)),
                ('goal_01_02', models.CharField(max_length=200, null=True)),
                ('goal_01_03', models.CharField(max_length=200, null=True)),
                ('goal_02_01', models.CharField(max_length=200, null=True)),
                ('goal_02_02', models.CharField(max_length=200, null=True)),
                ('goal_02_03', models.CharField(max_length=200, null=True)),
                ('goal_03_01', models.CharField(max_length=200, null=True)),
                ('goal_03_02', models.CharField(max_length=200, null=True)),
                ('goal_03_03', models.CharField(max_length=200, null=True)),
                ('goal_04_01', models.CharField(max_length=200, null=True)),
                ('goal_04_02', models.CharField(max_length=200, null=True)),
                ('goal_04_03', models.CharField(max_length=200, null=True)),
                ('goal_05_01', models.CharField(max_length=200, null=True)),
                ('goal_05_02', models.CharField(max_length=200, null=True)),
                ('goal_05_03', models.CharField(max_length=200, null=True)),
                ('goal_06_01', models.CharField(max_length=200, null=True)),
                ('goal_06_02', models.CharField(max_length=200, null=True)),
                ('goal_06_03', models.CharField(max_length=200, null=True)),
                ('goal_07_01', models.CharField(max_length=200, null=True)),
                ('goal_07_02', models.CharField(max_length=200, null=True)),
                ('goal_07_03', models.CharField(max_length=200, null=True)),
                ('goal_08_01', models.CharField(max_length=200, null=True)),
                ('goal_08_02', models.CharField(max_length=200, null=True)),
                ('goal_08_03', models.CharField(max_length=200, null=True)),
                ('goal_09_01', models.CharField(max_length=200, null=True)),
                ('goal_09_02', models.CharField(max_length=200, null=True)),
                ('goal_09_03', models.CharField(max_length=200, null=True)),
                ('goal_10_01', models.CharField(max_length=200, null=True)),
                ('goal_10_02', models.CharField(max_length=200, null=True)),
                ('goal_10_03', models.CharField(max_length=200, null=True)),
                ('goal_11_01', models.CharField(max_length=200, null=True)),
                ('goal_11_02', models.CharField(max_length=200, null=True)),
                ('goal_11_03', models.CharField(max_length=200, null=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='foreign_key')),
            ],
        ),
    ]
