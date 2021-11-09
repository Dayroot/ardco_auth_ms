# Generated by Django 3.2.9 on 2021-11-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fullname')),
                ('datebirth', models.DateField(blank=True, null=True, verbose_name='Datebirth')),
                ('email', models.EmailField(blank=True, max_length=320, null=True, verbose_name='Email')),
                ('identification', models.CharField(blank=True, max_length=15, null=True, verbose_name='Identification')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address')),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]