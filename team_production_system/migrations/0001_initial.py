# Generated by Django 4.1.7 on 2023-04-10 14:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={
                            'unique': 'A user with that username already exists.'
                        },
                        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name='username',
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='date joined'
                    ),
                ),
                ('is_mentor', models.BooleanField(default=False)),
                ('is_mentee', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=75, unique=True)),
                (
                    'phone_number',
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
                (
                    'profile_photo',
                    models.ImageField(blank=True, null=True, upload_to='profile_photo'),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ('team_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ('about_me', models.TextField(max_length=1000)),
                (
                    'skills',
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ('HTML', 'HTML'),
                            ('CSS', 'CSS'),
                            ('JavaScript', 'JavaScript'),
                            ('React', 'React'),
                            ('Python', 'Python'),
                            ('Django', 'Django'),
                            ('Django REST', 'Django REST'),
                        ],
                        max_length=52,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notifications',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('start_time', models.DateTimeField()),
                ('project', models.CharField(max_length=500)),
                ('help_text', models.TextField(max_length=500)),
                ('git_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('Pending', 'Pending'),
                            ('Confirmed', 'Confirmed'),
                            ('Canceled', 'Canceled'),
                            ('Completed', 'Completed'),
                        ],
                        default='Pending',
                        max_length=10,
                    ),
                ),
                (
                    'session_length',
                    models.IntegerField(
                        choices=[(30, '30 minutes'), (60, '60 minutes')], default=30
                    ),
                ),
                (
                    'mentor_availability',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='mentor_session',
                        to='team_production_system.availability',
                    ),
                ),
                (
                    'mentee',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='mentee_session',
                        to='team_production_system.mentee',
                    ),
                ),
                (
                    'mentor',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='mentor_session',
                        to='team_production_system.mentor',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='availability',
            name='mentor',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='mentor_availability',
                to='team_production_system.mentor',
            ),
        ),
    ]
