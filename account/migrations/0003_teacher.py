# Generated by Django 5.0.4 on 2024-05-03 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
        ('lessons', '0002_lesson_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lessons.subject')),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
        ),
    ]
