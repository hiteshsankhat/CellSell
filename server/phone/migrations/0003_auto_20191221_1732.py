# Generated by Django 2.2.7 on 2019-12-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_variant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='billAboveThreeMonth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='billBelowThreeMonth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='hasBox',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='hasCharger',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='hasHeadPhone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='isExcellent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='isFair',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='isNew',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='no_issue_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]