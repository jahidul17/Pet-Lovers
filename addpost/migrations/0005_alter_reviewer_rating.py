# Generated by Django 5.1.5 on 2025-02-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpost', '0004_alter_reviewer_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='rating',
            field=models.CharField(choices=[('⭐⭐⭐', '⭐⭐⭐'), ('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐')], max_length=10),
        ),
    ]
