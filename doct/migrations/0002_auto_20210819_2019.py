# Generated by Django 2.2.10 on 2021-08-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('doct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='max_patient',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField(blank=True, null=True)),
                ('Doctor', models.ManyToManyField(to='doct.Doctor')),
                ('patient', models.ManyToManyField(to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('problem', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=50)),
                ('doctor', models.ManyToManyField(to='doct.Doctor')),
                ('patient', models.ManyToManyField(to='patient.Patient')),
            ],
        ),
    ]
