# Generated by Django 2.0.5 on 2018-05-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='real_name',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='real_surname',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='subscribers',
            name='tel',
            field=models.CharField(default='SOME DIGITS', max_length=11),
        ),
    ]