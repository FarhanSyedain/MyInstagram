# Generated by Django 3.1.3 on 2020-12-25 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.FileField(upload_to='Data/Users/Posts')),
                ('tags', models.TextField(blank=True)),
                ('mentions', models.TextField(blank=True)),
                ('disciption', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ManyToManyField(blank=True, to='Config.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='Data/Users/Profiles')),
                ('bio', models.TextField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('profile_updated', models.DateTimeField(auto_now=True)),
                ('phone_number', models.IntegerField(blank=True)),
                ('country', models.CharField(blank=True, max_length=25, null=True)),
                ('followRequests', models.ManyToManyField(blank=True, related_name='_profile_followRequests_+', to='Config.Profile')),
                ('followRequestsSend', models.ManyToManyField(blank=True, related_name='_profile_followRequestsSend_+', to='Config.Profile')),
                ('followers', models.ManyToManyField(blank=True, related_name='_profile_followers_+', to='Config.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='_profile_following_+', to='Config.Profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.FileField(upload_to='Data/Users/Stories')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_posts', models.ManyToManyField(blank=True, related_name='posts', to='Config.Post')),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='bookmarked_in', to='Config.Post')),
                ('tagged', models.ManyToManyField(blank=True, related_name='tagged_in', to='Config.Post')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='people_tagged',
            field=models.ManyToManyField(blank=True, to='Config.Profile'),
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.profile')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Config.profile'),
        ),
    ]
