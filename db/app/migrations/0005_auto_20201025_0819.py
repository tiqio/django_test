# Generated by Django 3.1.1 on 2020-10-25 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201024_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='clas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.clas', verbose_name='班级(外键)'),
        ),
    ]
