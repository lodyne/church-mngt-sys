# Generated by Django 4.0.4 on 2022-05-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parish', '0002_alter_committee_role_alter_community_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='is_baptized',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_contributed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]