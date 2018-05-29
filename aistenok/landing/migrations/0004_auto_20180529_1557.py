# Generated by Django 2.0.5 on 2018-05-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20180528_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscribers', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='real_name',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='real_surname',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='addr',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='comment',
            field=models.CharField(default=None, max_length=512),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='login',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='pswrd',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='pswrd_again',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='surname',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='tel',
            field=models.CharField(default=None, max_length=12),
        ),
    ]