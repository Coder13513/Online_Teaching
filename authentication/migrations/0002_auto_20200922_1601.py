# Generated by Django 3.1.1 on 2020-09-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('TEACHER', 'teacher'), ('STUDENT', 'student')], default='ADMIN', max_length=20, verbose_name='user role'),
        ),
    ]