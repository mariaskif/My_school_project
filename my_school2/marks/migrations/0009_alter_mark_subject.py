# Generated by Django 4.1.2 on 2023-01-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('marks', '0008_mark_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='subjects.subject'),
        ),
    ]
