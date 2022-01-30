# Generated by Django 4.0.1 on 2022-01-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0002_country_coursetype_districts_states_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('mail_id', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('experience', models.IntegerField()),
                ('search_tags', models.CharField(max_length=400)),
                ('avatar', models.ImageField(upload_to='avatars')),
                ('resume', models.FileField(upload_to='resumes')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.course')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]