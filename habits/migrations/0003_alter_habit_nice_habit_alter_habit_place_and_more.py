# Generated by Django 5.1.3 on 2024-12-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="nice_habit",
            field=models.BooleanField(
                blank=True,
                default=True,
                null=True,
                verbose_name="Признак приятной привычки",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.CharField(
                blank=True,
                help_text="Укажите из какой области будет привычка",
                max_length=50,
                null=True,
                verbose_name="Место",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                blank=True,
                help_text="Установите время выполнения привычки",
                null=True,
                verbose_name="Время",
            ),
        ),
    ]
