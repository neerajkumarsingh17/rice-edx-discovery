# Generated by Django 1.9.11 on 2016-11-17 12:10


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0014_create_admin_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='preview_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserun',
            name='preview_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]