# Generated by Django 4.2 on 2024-07-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_mailing_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("COMPLETED", "Завершена"),
                    ("CREATED", "Создана"),
                    ("STARTED", "Запущена"),
                ],
                default="CREATED",
                max_length=50,
                verbose_name="статус",
            ),
        ),
        migrations.AlterField(
            model_name="trytosend",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.serviceclient",
                verbose_name="клиент",
            ),
        ),
    ]
