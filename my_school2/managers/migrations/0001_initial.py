# Generated by Django 4.1.2 on 2022-12-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('statrt_work', models.TimeField(auto_now=True)),
                ('end_work', models.TimeField(auto_now=True)),
            ],
            options={
                'db_table': 'managers',
            },
        ),
    ]
