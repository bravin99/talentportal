# Generated by Django 4.1.2 on 2022-10-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0005_job_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=models.SlugField(blank=True, help_text="Auto generated", unique=True),
        ),
    ]
