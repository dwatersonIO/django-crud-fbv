# Generated by Django 5.0.3 on 2024-03-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_options_remove_note_type_note_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='notes',
            field=models.ManyToManyField(blank=True, to='notes.note'),
        ),
    ]