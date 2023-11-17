# Generated by Django 4.2.7 on 2023-11-16 08:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exp_tracker", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("amount", models.FloatField(default=0)),
                ("date", models.DateField(default=datetime.date(2023, 11, 16))),
                ("long_term", models.BooleanField(default=False)),
                ("interest_rate", models.FloatField(blank=True, default=0, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "monthly_expense",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="account", name="expance_list",),
        migrations.AddField(
            model_name="account", name="balance", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="account", name="income", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="account", name="salary", field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="account",
            name="saving_goal",
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(name="Expence",),
        migrations.AddField(
            model_name="account",
            name="expense_list",
            field=models.ManyToManyField(blank=True, to="exp_tracker.expense"),
        ),
    ]
