# Generated by Django 3.2.4 on 2021-06-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20210613_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='boots',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='cpp',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='django',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='godot',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='htmlcss',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='js',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='php',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='python',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='wp',
        ),
        migrations.AddField(
            model_name='skills',
            name='darsad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]