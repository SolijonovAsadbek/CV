# Generated by Django 4.0.5 on 2022-06-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hi', models.CharField(max_length=30)),
                ('fullname', models.CharField(max_length=30)),
                ('about', models.TextField(max_length=200)),
                ('button', models.CharField(max_length=10)),
            ],
        ),
    ]