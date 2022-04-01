# Generated by Django 1.11.15 on 2018-11-28 19:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0069_move_has_ofac_restriction'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrupalLoaderConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_run_ids', models.TextField(blank=True, default=None, verbose_name='Course Run IDs')),
                ('partner_code', models.TextField(blank=True, default=None, verbose_name='Partner Code')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
