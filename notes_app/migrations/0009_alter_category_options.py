# Generated by Django 5.0.4 on 2024-05-04 14:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes_app", "0008_alter_note_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["name"], "verbose_name_plural": "Categories"},
        ),
    ]
