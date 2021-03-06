# Generated by Django 4.0.5 on 2022-06-17 06:22

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=200)),
                ('about_me', models.TextField(max_length=10000)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('birthday', models.DateTimeField(default=datetime.datetime(2022, 6, 17, 6, 22, 26, 979376, tzinfo=utc))),
                ('age', models.PositiveIntegerField(default=10)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Midlle', 'Midlle'), ('Senior', 'Senior')], default='Junior', max_length=7)),
                ('phone', models.CharField(default='+998', max_length=13)),
                ('city', models.CharField(choices=[('Namangan', 'Namangan'), ('Andijon', 'Andijon'), ('Farg`ona', 'Farg`ona'), ('Toshkent shahri', 'Toshkent shahri'), ('Toshkent viloyat', 'Toshkent viloyat'), ('Sirdaryo', 'Sirdaryo'), ('Qashqadaryo', 'Qashqadaryo'), ('Surxandaryo', 'Surxandaryo'), ('Navoiy', 'Navoiy'), ('Buxoro', 'Buxoro'), ('Xorazim', 'Xorazim'), ('Qoraqalpog`iston Respublikasi', 'Qoraqalpog`iston Respublikasi'), ('Samarqand', 'Samarqand')], default='Namangan', max_length=30)),
                ('freelance', models.BooleanField(default=False)),
                ('cv', models.FileField(upload_to='media/cv/')),
            ],
        ),
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
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('', ''), ('Python', 'Python'), ('Django', 'Django'), ('Flask', 'Flask'), ('JavaScript', 'JavaScript'), ('PHP', 'PHP'), ('Laravel', 'Laravel'), ('Java', 'Java'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('Bootstrap', 'Bootstrap'), ('C', 'C'), ('C++', 'C++')], default='', max_length=20)),
                ('protsent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('about_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_cv.about')),
            ],
        ),
    ]
