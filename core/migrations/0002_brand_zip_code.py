# Generated by Django 4.1.3 on 2022-11-18 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='zip_code',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.zipcode'),
            preserve_default=False,
        ),
    ]
