import django.db.models.deletion
import django_extensions.db.fields
import sortedm2m.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20160510_2017'),
        ('ietf_language_tags', '0002_language_tag_data_migration'),
        ('course_metadata', '0001_squashed_0033_courserun_mobile_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(default=None, null=True, blank=True, max_length=255)),
                ('number', models.CharField(null=True, blank=True, max_length=50)),
                ('short_description', models.CharField(default=None, null=True, blank=True, max_length=255)),
                ('full_description', models.TextField(default=None, null=True, blank=True)),
                ('expected_learnings', models.TextField(default=None, null=True, blank=True)),
                ('syllabus', models.TextField(default=None, null=True, blank=True)),
                ('prerequisites', models.TextField(default=None, null=True, blank=True)),
                ('learner_testimonial', models.CharField(null=True, blank=True, max_length=50)),
                ('level_type', models.ForeignKey(related_name='publisher_courses', to='course_metadata.LevelType', default=None, null=True, blank=True, on_delete=django.db.models.deletion.CASCADE)),
                ('organizations', models.ManyToManyField(related_name='publisher_courses', blank=True, to='course_metadata.Organization')),
                ('primary_subject', models.ForeignKey(related_name='publisher_courses_primary', to='course_metadata.Subject', on_delete=django.db.models.deletion.CASCADE)),
                ('secondary_subject', models.ForeignKey(related_name='publisher_courses_secondary', to='course_metadata.Subject', on_delete=django.db.models.deletion.CASCADE)),
                ('tertiary_subject', models.ForeignKey(related_name='publisher_courses_tertiary', to='course_metadata.Subject', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseRun',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('lms_course_id', models.CharField(unique=True, null=True, blank=True, max_length=255)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('enrollment_start', models.DateTimeField(null=True, blank=True)),
                ('enrollment_end', models.DateTimeField(null=True, blank=True)),
                ('certificate_generation', models.DateTimeField(null=True, blank=True)),
                ('pacing_type', models.CharField(choices=[('self_paced', 'Self-paced'), ('instructor_paced', 'Instructor-paced')], null=True, blank=True, db_index=True, max_length=255)),
                ('min_effort', models.PositiveSmallIntegerField(help_text='Estimated minimum number of hours per week needed to complete a course run.', null=True, blank=True)),
                ('max_effort', models.PositiveSmallIntegerField(help_text='Estimated maximum number of hours per week needed to complete a course run.', null=True, blank=True)),
                ('length', models.PositiveIntegerField(help_text='Length of course, in number of weeks', null=True, blank=True)),
                ('is_re_run', models.BooleanField(default=False)),
                ('is_xseries', models.BooleanField(default=False)),
                ('xseries_name', models.CharField(max_length=255)),
                ('is_micromasters', models.BooleanField(default=False)),
                ('micromasters_name', models.CharField(max_length=255)),
                ('contacted_partner_manager', models.BooleanField(default=False)),
                ('seo_review', models.TextField(help_text='SEO review on your course title and short description', default=None, null=True, blank=True)),
                ('keywords', models.TextField(help_text='Please add top 10 comma separated keywords for your course content', default=None, blank=True)),
                ('notes', models.TextField(help_text='Please add any additional notes or special instructions for the course About Page.', default=None, null=True, blank=True)),
                ('target_content', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3'), ('L4', 'Level 4'), ('L5', 'Level 5')], null=True, blank=True, max_length=5)),
                ('course_team_admins', models.TextField(help_text='Comma separated list of edX usernames or emails of admins.', default=None, null=True, blank=True)),
                ('course_team_additional_staff', models.TextField(help_text='Comma separated list of edX usernames or emails of additional staff.', default=None, null=True, blank=True)),
                ('course', models.ForeignKey(to='publisher.Course', on_delete=django.db.models.deletion.CASCADE)),
                ('language', models.ForeignKey(related_name='publisher_course_runs', to='ietf_language_tags.LanguageTag', null=True, blank=True, on_delete=django.db.models.deletion.CASCADE)),
                ('sponsor', models.ManyToManyField(related_name='publisher_course_runs', blank=True, to='course_metadata.Organization')),
                ('staff', sortedm2m.fields.SortedManyToManyField(related_name='publisher_course_runs_staffed', help_text=None, blank=True, to='course_metadata.Person')),
                ('transcript_languages', models.ManyToManyField(related_name='publisher_transcript_course_runs', blank=True, to='ietf_language_tags.LanguageTag')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCourse',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', auto_created=True, db_index=True, blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(default=None, null=True, blank=True, max_length=255)),
                ('number', models.CharField(null=True, blank=True, max_length=50)),
                ('short_description', models.CharField(default=None, null=True, blank=True, max_length=255)),
                ('full_description', models.TextField(default=None, null=True, blank=True)),
                ('expected_learnings', models.TextField(default=None, null=True, blank=True)),
                ('syllabus', models.TextField(default=None, null=True, blank=True)),
                ('prerequisites', models.TextField(default=None, null=True, blank=True)),
                ('learner_testimonial', models.CharField(null=True, blank=True, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('level_type', models.ForeignKey(related_name='+', db_constraint=False, to='course_metadata.LevelType', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('primary_subject', models.ForeignKey(related_name='+', db_constraint=False, to='course_metadata.Subject', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('secondary_subject', models.ForeignKey(related_name='+', db_constraint=False, to='course_metadata.Subject', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('tertiary_subject', models.ForeignKey(related_name='+', db_constraint=False, to='course_metadata.Subject', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical course',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourseRun',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', auto_created=True, db_index=True, blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('lms_course_id', models.CharField(null=True, blank=True, db_index=True, max_length=255)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('enrollment_start', models.DateTimeField(null=True, blank=True)),
                ('enrollment_end', models.DateTimeField(null=True, blank=True)),
                ('certificate_generation', models.DateTimeField(null=True, blank=True)),
                ('pacing_type', models.CharField(choices=[('self_paced', 'Self-paced'), ('instructor_paced', 'Instructor-paced')], null=True, blank=True, db_index=True, max_length=255)),
                ('min_effort', models.PositiveSmallIntegerField(help_text='Estimated minimum number of hours per week needed to complete a course run.', null=True, blank=True)),
                ('max_effort', models.PositiveSmallIntegerField(help_text='Estimated maximum number of hours per week needed to complete a course run.', null=True, blank=True)),
                ('length', models.PositiveIntegerField(help_text='Length of course, in number of weeks', null=True, blank=True)),
                ('is_re_run', models.BooleanField(default=False)),
                ('is_xseries', models.BooleanField(default=False)),
                ('xseries_name', models.CharField(max_length=255)),
                ('is_micromasters', models.BooleanField(default=False)),
                ('micromasters_name', models.CharField(max_length=255)),
                ('contacted_partner_manager', models.BooleanField(default=False)),
                ('seo_review', models.TextField(help_text='SEO review on your course title and short description', default=None, null=True, blank=True)),
                ('keywords', models.TextField(help_text='Please add top 10 comma separated keywords for your course content', default=None, blank=True)),
                ('notes', models.TextField(help_text='Please add any additional notes or special instructions for the course About Page.', default=None, null=True, blank=True)),
                ('target_content', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2'), ('L3', 'Level 3'), ('L4', 'Level 4'), ('L5', 'Level 5')], null=True, blank=True, max_length=5)),
                ('course_team_admins', models.TextField(help_text='Comma separated list of edX usernames or emails of admins.', default=None, null=True, blank=True)),
                ('course_team_additional_staff', models.TextField(help_text='Comma separated list of edX usernames or emails of additional staff.', default=None, null=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course', models.ForeignKey(related_name='+', db_constraint=False, to='publisher.Course', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('language', models.ForeignKey(related_name='+', db_constraint=False, to='ietf_language_tags.LanguageTag', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical course run',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSeat',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', auto_created=True, db_index=True, blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.CharField(choices=[('honor', 'Honor'), ('audit', 'Audit'), ('verified', 'Verified'), ('professional', 'Professional (with ID verification)'), ('no-id-professional', 'Professional (no ID verifiation)'), ('credit', 'Credit')], max_length=63)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('upgrade_deadline', models.DateTimeField(null=True, blank=True)),
                ('credit_provider', models.CharField(null=True, blank=True, max_length=255)),
                ('credit_hours', models.IntegerField(null=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course_run', models.ForeignKey(related_name='+', db_constraint=False, to='publisher.CourseRun', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('currency', models.ForeignKey(related_name='+', db_constraint=False, to='core.Currency', null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical seat',
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.CharField(choices=[('honor', 'Honor'), ('audit', 'Audit'), ('verified', 'Verified'), ('professional', 'Professional (with ID verification)'), ('no-id-professional', 'Professional (no ID verifiation)'), ('credit', 'Credit')], max_length=63)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('upgrade_deadline', models.DateTimeField(null=True, blank=True)),
                ('credit_provider', models.CharField(null=True, blank=True, max_length=255)),
                ('credit_hours', models.IntegerField(null=True, blank=True)),
                ('course_run', models.ForeignKey(related_name='seats', to='publisher.CourseRun', on_delete=django.db.models.deletion.CASCADE)),
                ('currency', models.ForeignKey(related_name='publisher_seats', to='core.Currency', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]