# Generated by Django 2.1.1 on 2018-09-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180906_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
    ]
