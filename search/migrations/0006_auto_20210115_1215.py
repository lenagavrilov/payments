# Generated by Django 2.1.15 on 2021-01-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20210115_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='checkBook',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='alternativeSupplyer',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='checkNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='givenInstead',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='givenOutDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='paymentNumberInSeries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='quantityinSeries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='refuseDate',
            field=models.DateField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='refuseReason',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
