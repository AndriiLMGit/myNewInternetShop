# Generated by Django 3.0.7 on 2021-01-19 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_brand', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('White', 'White'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Purple', 'Purple')], default='White', max_length=50)),
                ('image_thumbnail', models.FileField(upload_to='men/t_shirts/thumbnail/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='men.MenCategory')),
            ],
        ),
    ]