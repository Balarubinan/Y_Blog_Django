# Generated by Django 3.1.5 on 2021-06-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_html', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('media_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='media_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cus', models.IntegerField()),
                ('data', models.BinaryField()),
            ],
        ),
    ]
