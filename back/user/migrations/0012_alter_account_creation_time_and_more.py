# Generated by Django 4.0.4 on 2022-05-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_vault_balance_alter_vault_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]