# Generated by Django 5.0.6 on 2024-05-23 09:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]