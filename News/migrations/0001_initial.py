# Generated by Django 3.0.6 on 2020-06-16 02:35

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
            name='Column',
            fields=[
                ('cl_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cl_name', models.CharField(max_length=64)),
                ('cl_description', models.TextField(blank=True, max_length=512)),
                ('cl_gen_time', models.DateTimeField(auto_now_add=True)),
                ('parent_cl_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='News.Column')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cmt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_reliable', models.IntegerField(choices=[(0, '内容违规'), (1, '收到举报'), (2, '正在审核'), (3, '正常')], default=3)),
                ('cmt_content', models.TextField(max_length=1024)),
                ('cmt_gen_time', models.DateTimeField(auto_now_add=True)),
                ('like_num', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('files_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('files_name', models.CharField(max_length=64)),
                ('files_title', models.CharField(max_length=64)),
                ('files_path', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('img_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img_name', models.CharField(max_length=64)),
                ('img_title', models.CharField(max_length=64)),
                ('img_path', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=64)),
                ('news_url', models.URLField()),
                ('news_gen_time', models.DateTimeField(auto_now_add=True)),
                ('view_num', models.BigIntegerField(default=0)),
                ('share_num', models.BigIntegerField(default=0)),
                ('cmt_num', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShareNews',
            fields=[
                ('share_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('share_text', models.TextField(blank=True, max_length=512)),
                ('share_time', models.DateTimeField(auto_now_add=True)),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublishNews',
            fields=[
                ('pub_news_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublishComments',
            fields=[
                ('pub_cmt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cmt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Comment')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('news_files_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Images')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
        migrations.CreateModel(
            name='NewsFiles',
            fields=[
                ('news_files_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('files_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Files')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
        migrations.CreateModel(
            name='NewsComments',
            fields=[
                ('news_cmt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cmt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Comment')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
        migrations.CreateModel(
            name='NewsColumn',
            fields=[
                ('news_cl_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Column')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.News')),
            ],
        ),
        migrations.CreateModel(
            name='JudgeComment',
            fields=[
                ('judge_cmt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('report_text', models.TextField(default=None, max_length=1024, null=True)),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('report_type', models.IntegerField(choices=[(0, '点赞'), (1, '举报')], default=0)),
                ('cmt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.Comment')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
