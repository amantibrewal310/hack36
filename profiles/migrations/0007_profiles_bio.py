# Generated by Django 2.2.4 on 2020-02-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200215_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='bio',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]