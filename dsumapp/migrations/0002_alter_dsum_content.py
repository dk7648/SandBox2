# Generated by Django 3.2.5 on 2021-07-24 07:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsumapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsum',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]