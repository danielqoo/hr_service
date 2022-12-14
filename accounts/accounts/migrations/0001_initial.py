# Generated by Django 3.2.9 on 2021-12-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('comingday', models.DateField()),
                ('organization', models.CharField(max_length=30, verbose_name='organization')),
                ('department', models.CharField(max_length=30, verbose_name='department')),
                ('team', models.CharField(max_length=30, verbose_name='team')),
                ('level', models.CharField(max_length=30, verbose_name='level')),
                ('phonenumber', models.CharField(max_length=30, verbose_name='phonenumber')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
