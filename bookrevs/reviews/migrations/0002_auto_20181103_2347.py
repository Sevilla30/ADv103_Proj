# Generated by Django 2.1.2 on 2018-11-03 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='wine',
            new_name='book',
        ),
    ]
