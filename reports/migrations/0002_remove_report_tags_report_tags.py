# Generated by Django 4.1.3 on 2022-12-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='tags',
        ),
        migrations.AddField(
            model_name='report',
            name='tags',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='reports.tag'),
            preserve_default=False,
        ),
    ]
