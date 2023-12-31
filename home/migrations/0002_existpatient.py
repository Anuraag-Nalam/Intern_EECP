# Generated by Django 3.0.4 on 2020-08-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Existpatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpsys', models.CharField(max_length=22)),
                ('bpdia', models.CharField(max_length=22)),
                ('visceralfatlevel', models.CharField(max_length=122)),
                ('restingmetabolism', models.CharField(max_length=122)),
                ('bmi', models.CharField(max_length=122)),
                ('bfp', models.CharField(max_length=122)),
                ('bodytemperature', models.CharField(max_length=122)),
                ('skeletalmusclepercentage', models.CharField(max_length=122)),
                ('footbottom', models.ImageField(upload_to='')),
                ('foottop', models.ImageField(upload_to='')),
                ('legs', models.ImageField(upload_to='')),
                ('handsfront', models.ImageField(upload_to='')),
                ('handsback', models.ImageField(upload_to='')),
                ('lefteye', models.ImageField(upload_to='')),
                ('righteye', models.ImageField(upload_to='')),
                ('pulse', models.ImageField(max_length=122, upload_to='')),
                ('weight', models.ImageField(max_length=122, upload_to='')),
                ('roomhumidity', models.ImageField(max_length=122, upload_to='')),
                ('roomtemperature', models.ImageField(max_length=122, upload_to='')),
            ],
        ),
    ]
