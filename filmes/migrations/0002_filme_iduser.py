# Generated by Django 5.1 on 2024-11-19 11:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='iduser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='filmes_cadastrados', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
