# Generated by Django 3.1.4 on 2021-02-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210203_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ManyToManyField(blank=True, null=True, to='home.Aseat'),
        ),
    ]
