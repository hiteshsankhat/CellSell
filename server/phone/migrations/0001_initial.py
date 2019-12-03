# Generated by Django 2.2.7 on 2019-12-03 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ModelNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=500)),
                ('brandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.BrandName')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veriantName', models.CharField(max_length=500)),
                ('modelNumberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.ModelNumber')),
            ],
        ),
    ]
