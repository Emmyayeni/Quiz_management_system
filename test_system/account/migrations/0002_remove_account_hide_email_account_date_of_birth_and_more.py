# Generated by Django 4.2.3 on 2023-09-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="hide_email",
        ),
        migrations.AddField(
            model_name="account",
            name="date_of_birth",
            field=models.DateField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="account",
            name="number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
