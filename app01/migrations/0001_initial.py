# Generated by Django 2.1.8 on 2019-08-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
    ]
