# Generated by Django 3.2.7 on 2022-02-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_loanform'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanform',
            name='userform',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
