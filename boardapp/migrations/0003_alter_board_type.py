# Generated by Django 3.2.5 on 2021-07-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_board_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.CharField(choices=[('notice', '공지사항'), ('dsum', 'D-SUM'), ('kquestion', '전공 1000제'), ('contest', '공모전'), ('tutoring', '전공튜터링')], max_length=10, null=True),
        ),
    ]
