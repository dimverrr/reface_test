# Generated by Django 5.0.4 on 2024-05-07 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes_app", "0012_category_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["title"], "verbose_name_plural": "Categories"},
        ),
        migrations.RenameField(
            model_name="category",
            old_name="name",
            new_name="title",
        ),
    ]