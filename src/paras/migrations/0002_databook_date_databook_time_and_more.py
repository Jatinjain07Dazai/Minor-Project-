# Generated by Django 4.1.7 on 2023-04-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='databook',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='databook',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='databook',
            name='input_text',
            field=models.TextField(),
        ),
    ]
