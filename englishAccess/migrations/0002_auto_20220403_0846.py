# Generated by Django 3.2.9 on 2022-04-03 08:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('englishAccess', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='Languages',
        ),
        migrations.RenameModel(
            old_name='Therapist',
            new_name='Therapists',
        ),
    ]