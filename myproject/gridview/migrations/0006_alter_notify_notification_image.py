# Generated by Django 4.2 on 2023-04-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridview', '0005_alter_notify_notication_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='notification_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
