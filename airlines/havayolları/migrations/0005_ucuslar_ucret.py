# Generated by Django 5.0.4 on 2024-05-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('havayolları', '0004_havaalanlari_kod_alter_ucuslar_kalkis_havaalani_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucuslar',
            name='ucret',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
