# Generated by Django 4.2.9 on 2024-02-11 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
