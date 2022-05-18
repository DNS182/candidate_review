# Generated by Django 4.0.4 on 2022-05-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Contact', models.IntegerField()),
                ('Email', models.EmailField(max_length=40)),
                ('Country', models.CharField(max_length=20)),
                ('Degree', models.CharField(max_length=40)),
                ('Position', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=40)),
                ('Resume', models.FileField(blank=True, upload_to='static/resume/')),
                ('Applied_for', models.CharField(max_length=40)),
                ('Applied_on', models.DateTimeField()),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
    ]