# Generated by Django 3.0.4 on 2020-03-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]