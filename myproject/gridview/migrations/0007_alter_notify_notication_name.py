# Generated by Django 4.2 on 2023-04-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridview', '0006_alter_notify_notification_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='notication_name',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]