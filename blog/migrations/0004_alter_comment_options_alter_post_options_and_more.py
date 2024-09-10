# Generated by Django 4.2.16 on 2024-09-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_updated_on_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='field_1',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
