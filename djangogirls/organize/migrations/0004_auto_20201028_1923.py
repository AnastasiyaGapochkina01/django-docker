# Generated by Django 2.0.12 on 2020-10-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organize', '0003_auto_20190727_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplication',
            name='remote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventapplication',
            name='safety',
            field=models.TextField(blank=True, verbose_name="Information about how you will ensure participants' and coaches' safety during the Covid-19 pandemic"),
        ),
        migrations.AddField(
            model_name='eventapplication',
            name='tools',
            field=models.TextField(blank=True, verbose_name='Information about how you will host your remote workshop'),
        ),
        migrations.AlterField(
            model_name='eventapplication',
            name='venue',
            field=models.TextField(blank=True, verbose_name='Information about your potential venue'),
        ),
    ]
