# Generated by Django 3.0.4 on 2020-09-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_afterpatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientid', models.CharField(default='', max_length=10)),
                ('averageecg', models.CharField(default='', max_length=10)),
                ('averageso', models.CharField(max_length=22)),
                ('averagepeakratio', models.CharField(max_length=22)),
                ('averagearearatio', models.CharField(max_length=122)),
                ('pressure', models.CharField(max_length=122)),
            ],
        ),
    ]
