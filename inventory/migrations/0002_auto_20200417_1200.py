# Generated by Django 3.0.5 on 2020-04-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='issues',
            field=models.CharField(default='No issues', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='issues',
            field=models.CharField(default='No issues', max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='issues',
            field=models.CharField(default='No issues', max_length=100),
        ),
    ]
