# Generated by Django 5.1 on 2024-10-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='class_period',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='weeks',
            field=models.CharField(max_length=50),
        ),
    ]
