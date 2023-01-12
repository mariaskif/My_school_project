# Generated by Django 4.1.2 on 2022-12-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('marks', '0007_remove_mark_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.OneToOneField(default=5555, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='subjects.subject'),
            preserve_default=False,
        ),
    ]
