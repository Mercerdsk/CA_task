# Generated by Django 4.2 on 2023-04-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridview', '0003_alter_notify_notication_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='notication_name',
            field=models.CharField(blank=True, default='null', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notify',
            name='notification_image',
            field=models.CharField(blank=True, default='null', max_length=1000, null=True),
        ),
    ]
