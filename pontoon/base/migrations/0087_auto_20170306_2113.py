# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0086_auto_20170303_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='info_brief',
            new_name='info',
        ),
        migrations.AddField(
            model_name='locale',
            name='style_guide',
            field=models.URLField(blank=True, help_text=b'\n        URL to style guide for this locale.\n    '),
        ),
        migrations.AddField(
            model_name='project',
            name='can_be_requested',
            field=models.BooleanField(default=True, help_text=b'\n        Allow localizers to request the project for their team.\n    '),
        ),
        migrations.AddField(
            model_name='project',
            name='l10n_contact',
            field=models.ForeignKey(blank=True, help_text=b'\n        L10n driver in charge of the project.\n    ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l10n_contact_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='preview_url',
            field=models.URLField(blank=True, help_text=b'\n        URL to translation preview environment, e.g. staging website,\n        screenshots, development build, etc.\n    ', verbose_name=b'L10n Preview URL'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_contact',
            field=models.ForeignKey(blank=True, help_text=b'\n        Project manager or developer contact.\n    ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_contact_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(blank=True, help_text=b'\n        URL to released project, e.g. production website or product download.\n    ', verbose_name=b'Project URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='disabled',
            field=models.BooleanField(default=False, help_text=b'\n        Hide project from the UI and only keep it accessible from the admin.\n        Disable the project instead of deleting it to keep translation memory\n        and attributions.\n    '),
        ),
    ]
