# Generated by Django 2.1.15 on 2021-02-12 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20210212_0823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentskind',
            options={'ordering': ['definition']},
        ),
    ]