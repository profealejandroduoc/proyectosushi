# Generated by Django 5.0.6 on 2024-06-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sushi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='producto',
            new_name='nombre_producto',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]