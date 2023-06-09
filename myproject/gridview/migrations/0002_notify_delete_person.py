# Generated by Django 4.2 on 2023-04-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_title', models.CharField(max_length=100)),
                ('notification_text', models.CharField(max_length=500)),
                ('notification_image', models.CharField(max_length=1000)),
                ('notication_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
