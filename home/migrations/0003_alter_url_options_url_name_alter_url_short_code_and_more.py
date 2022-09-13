# Generated by Django 4.1 on 2022-09-13 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0002_alter_url_short_code_remove_userdata_url_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="url",
            options={
                "verbose_name": "UserData",
                "verbose_name_plural": "UserData Details",
            },
        ),
        migrations.AddField(
            model_name="url",
            name="name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="url",
            name="short_code",
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name="UserData",
        ),
    ]
