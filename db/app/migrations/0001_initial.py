# Generated by Django 3.1.1 on 2020-10-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('score', models.FloatField(blank=True, null=True, verbose_name='成绩')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='年级')),
            ],
        ),
    ]