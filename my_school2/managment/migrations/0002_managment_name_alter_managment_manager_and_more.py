# Generated by Django 4.1.2 on 2022-12-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managment',
            name='name',
            field=models.CharField(default='fff', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='managment',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_manager', to='managers.manager'),
        ),
        migrations.AlterModelTable(
            name='managment',
            table='section',
        ),
    ]