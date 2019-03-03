# Generated by Django 2.1.7 on 2019-03-03 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20190303_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='aadharModel',
            fields=[
                ('aadhar', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='generalPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('image_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.imageModel')),
                ('uni_adhaar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.aadharModel')),
            ],
        ),
    ]