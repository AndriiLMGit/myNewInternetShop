# Generated by Django 3.0.7 on 2020-11-30 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0002_auto_20201130_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentbag',
            name='bag_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bags.Bag'),
        ),
    ]
