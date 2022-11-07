# Generated by Django 4.1.1 on 2022-10-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0011_logentry_serialized_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="action",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "create"), (1, "update"), (2, "delete"), (3, "access")],
                db_index=True,
                verbose_name="action",
            ),
        ),
    ]
