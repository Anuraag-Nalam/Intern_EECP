# Generated by Django 3.0.4 on 2020-09-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200903_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpatient',
            name='allergic',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='diabetes',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='heartproblem',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='hospitalization',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='hypertension',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='medication',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='surgery',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newpatient',
            name='thyroid',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
