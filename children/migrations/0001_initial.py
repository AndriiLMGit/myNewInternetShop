# Generated by Django 3.0.7 on 2020-12-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrenThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_children_thing', models.CharField(max_length=30)),
                ('new_price_children_thing', models.PositiveIntegerField()),
                ('old_price_children_thing', models.PositiveIntegerField()),
                ('describe_children_thing', models.TextField()),
                ('front_image_children_thing', models.FileField(upload_to='children/title')),
                ('back_image_children_thing', models.FileField(upload_to='children/title')),
                ('big_detail_image_children_thing', models.FileField(upload_to='children/detail')),
                ('middle_1_detail_image_children_thing', models.FileField(upload_to='children/detail')),
                ('middle_2_detail_image_children_thing', models.FileField(upload_to='children/detail')),
                ('children_published_at', models.DateTimeField()),
            ],
        ),
    ]