# Generated by Django 5.0.4 on 2024-05-04 19:26

import colorfield.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notes_app", "0010_alter_note_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="user",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF",
                image_field=None,
                max_length=25,
                samples=None,
                unique=True,
            ),
        ),
    ]
