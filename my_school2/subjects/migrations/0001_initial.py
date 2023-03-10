# Generated by Django 4.1.2 on 2022-12-21 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labrotaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('mark', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
                ('part', models.IntegerField(default=0)),
                ('labrotary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labrotaries.labrotary')),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
    ]
