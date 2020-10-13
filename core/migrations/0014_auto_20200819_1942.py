# Generated by Django 3.0.8 on 2020-08-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marksheet',
            name='final_grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='marksheet',
            name='final_term_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marksheet',
            name='mid_term_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]