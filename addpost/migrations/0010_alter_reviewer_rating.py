# Generated by Django 5.1.5 on 2025-02-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpost', '0009_post_author_post_created_at_alter_reviewer_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='rating',
            field=models.CharField(choices=[('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐')], max_length=10),
        ),
    ]
