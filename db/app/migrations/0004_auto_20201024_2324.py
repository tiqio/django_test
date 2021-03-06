# Generated by Django 3.1.1 on 2020-10-24 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201024_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='人数')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='clas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.clas', verbose_name='外键'),
        ),
    ]
