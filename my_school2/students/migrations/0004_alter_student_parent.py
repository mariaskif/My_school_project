# Generated by Django 4.1.2 on 2023-01-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
        ('students', '0003_alter_student_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.parent'),
        ),
    ]
