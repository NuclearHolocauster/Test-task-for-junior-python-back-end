# Generated by Django 4.0.2 on 2022-03-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]