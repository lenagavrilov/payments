# Generated by Django 2.1.15 on 2021-01-15 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20210115_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='alternativeSupplier',
            new_name='alternativeSupplyer',
        ),
    ]