# Generated by Django 2.1.8 on 2019-08-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24, verbose_name='出版社名称')),
            ],
        ),
    ]