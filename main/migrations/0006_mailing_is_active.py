# Generated by Django 4.2 on 2024-07-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_mailing_next_send_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Блокировка Рассылки"),
        ),
    ]
