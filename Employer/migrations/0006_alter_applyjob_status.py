# Generated by Django 4.0.1 on 2022-02-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0005_alter_job_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(default='submitted', max_length=20),
        ),
    ]
