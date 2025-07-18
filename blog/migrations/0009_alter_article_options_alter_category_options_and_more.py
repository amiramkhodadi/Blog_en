# Generated by Django 5.2 on 2025-07-17 07:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': ' مقاله ', 'verbose_name_plural': 'مقالات '},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '  دسته بندی ', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': ' نظر ', 'verbose_name_plural': 'نظرات '},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': ' پیام ', 'verbose_name_plural': ' پیام ها  '},
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'لایک',
                'verbose_name_plural': 'لایک ها ',
                'ordering': ['-created_date'],
            },
        ),
    ]
