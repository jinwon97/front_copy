# Generated by Django 4.2 on 2023-12-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("admin_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=75, unique=True)),
                ("password", models.CharField(max_length=75)),
            ],
            options={
                "db_table": "admin",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=75, unique=True)),
                ("password", models.CharField(max_length=75)),
                ("email", models.CharField(max_length=254)),
                ("phonenumber", models.CharField(max_length=11)),
                ("age", models.PositiveIntegerField()),
                ("gender", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "user",
                "managed": False,
            },
        ),
    ]
