# Generated by Django 4.0.1 on 2022-02-04 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MetaData', '0001_initial'),
        ('Account', '0005_remove_employee_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('company_type', models.CharField(max_length=50)),
                ('about_company', models.TextField()),
                ('status', models.CharField(default='pending', max_length=10)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MetaData.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
