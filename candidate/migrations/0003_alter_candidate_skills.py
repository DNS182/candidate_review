# Generated by Django 4.0.4 on 2022-05-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_candidate_skills_alter_candidate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='Skills',
            field=models.TextField(unique=True),
        ),
    ]
