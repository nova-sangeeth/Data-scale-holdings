# Generated by Django 3.1 on 2020-08-11 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='educational_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters/Post-Graduation', 'Masters/Post-Graduation'), ('10th', '10th'), ('12th', '12th')], max_length=64, null=True)),
                ('course', models.CharField(max_length=64, null=True)),
                ('specialization', models.CharField(max_length=64, null=True)),
                ('university_or_institute', models.CharField(max_length=64, null=True)),
                ('course_type', models.CharField(choices=[('full_Time', 'full_time'), ('part_time', 'part_time')], max_length=64, null=True)),
                ('Date_of_passing_out', models.DateField(null=True)),
                ('percentage_or_grade_accquired', models.CharField(max_length=64, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
