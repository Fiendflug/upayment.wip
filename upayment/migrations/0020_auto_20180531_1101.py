# Generated by Django 2.0.2 on 2018-05-31 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upayment', '0019_internet_tarif_mts_tarif'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MTS_tarif',
            new_name='phone_tarif',
        ),
    ]
