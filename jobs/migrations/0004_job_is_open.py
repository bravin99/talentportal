# Generated by Django 4.1.2 on 2022-10-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_job_contract_type_job_job_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="is_open",
            field=models.BooleanField(default=True),
        ),
    ]
