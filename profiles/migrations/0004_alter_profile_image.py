# Generated by Django 3.2.22 on 2023-11-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_bst2p6', upload_to='images/'),
        ),
    ]
