# Generated by Django 4.1.2 on 2022-10-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="positions",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="job",
            name="salary",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
    ]
