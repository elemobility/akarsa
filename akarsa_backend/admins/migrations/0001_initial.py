# Generated by Django 3.1.13 on 2022-02-23 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=15)),
                ('country_code', models.IntegerField()),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(upload_to='customer/profile_image')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('otp', models.CharField(max_length=200)),
                ('is_user_blocked', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
            ],
        ),
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Faq_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='General_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('tagline', models.CharField(max_length=30)),
                ('website_url', models.CharField(blank=True, max_length=3, null=True)),
                ('company_email', models.EmailField(max_length=60, verbose_name='email')),
                ('company_country_code', models.CharField(max_length=10)),
                ('company_phone_no', models.CharField(max_length=20)),
                ('company_address_line_1', models.CharField(max_length=200)),
                ('company_address_line_2', models.CharField(max_length=200)),
                ('company_city', models.CharField(max_length=100)),
                ('company_state', models.CharField(max_length=100)),
                ('company_zip_code', models.CharField(max_length=100)),
                ('company_country', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to='akarsa')),
                ('cin_no', models.CharField(blank=True, max_length=200, null=True)),
                ('gstin_no', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social_media_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appstore_link', models.CharField(max_length=2000)),
                ('playstore_link', models.CharField(max_length=2000)),
                ('company_url', models.CharField(max_length=2000)),
                ('facebook_url', models.CharField(max_length=2000)),
                ('twitter_url', models.CharField(max_length=2000)),
                ('instagram_url', models.CharField(max_length=2000)),
                ('linkedin_url', models.CharField(max_length=2000)),
                ('youtube_url', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='admins.faq_category')),
            ],
        ),
    ]