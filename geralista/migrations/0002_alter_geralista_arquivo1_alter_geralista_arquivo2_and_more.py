# Generated by Django 4.1 on 2022-10-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geralista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geralista',
            name='arquivo1',
            field=models.FileField(blank=True, null=True, upload_to='arquivo1/', verbose_name='arquivo1'),
        ),
        migrations.AlterField(
            model_name='geralista',
            name='arquivo2',
            field=models.FileField(blank=True, null=True, upload_to='arquivo2/', verbose_name='arquivo1'),
        ),
        migrations.AlterField(
            model_name='geralista',
            name='arquivo3',
            field=models.FileField(blank=True, null=True, upload_to='arquivo3/', verbose_name='arquivo1'),
        ),
    ]
