# Generated by Django 4.2.16 on 2024-09-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_challenge_alter_post_field_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
    ]
