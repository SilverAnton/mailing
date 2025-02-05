# Generated by Django 4.2 on 2024-07-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [("can_edit_is_active", "can edit is active")],
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                blank=True, default=True, null=True, verbose_name="is_active status"
            ),
        ),
    ]
