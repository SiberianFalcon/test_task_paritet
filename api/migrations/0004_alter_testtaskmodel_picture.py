# Generated by Django 5.0.7 on 2024-07-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_testtaskmodel_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testtaskmodel",
            name="picture",
            field=models.ImageField(default=1, upload_to="images"),
            preserve_default=False,
        ),
    ]