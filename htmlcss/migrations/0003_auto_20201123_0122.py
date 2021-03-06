# Generated by Django 3.1.2 on 2020-11-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0002_auto_20201120_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customermore',
            name='idNum',
        ),
        migrations.RemoveField(
            model_name='restaurantmore',
            name='einNum',
        ),
        migrations.AddField(
            model_name='user',
            name='idNum',
            field=models.CharField(blank=True, max_length=13, verbose_name='idNum'),
        ),
        migrations.AlterField(
            model_name='restaurantmore',
            name='busAddress',
            field=models.CharField(max_length=90, null=True, verbose_name='busAddress'),
        ),
        migrations.AlterField(
            model_name='restaurantmore',
            name='busName',
            field=models.CharField(max_length=50, verbose_name='busName'),
        ),
    ]
