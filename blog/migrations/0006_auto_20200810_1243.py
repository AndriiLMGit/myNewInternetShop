# Generated by Django 3.0.7 on 2020-08-10 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200810_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentblogpost',
            options={'ordering': ('-created',)},
        ),
    ]