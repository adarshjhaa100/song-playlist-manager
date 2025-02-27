# Generated by Django 5.1.6 on 2025-02-27 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('danceability', models.FloatField()),
                ('energy', models.FloatField()),
                ('mode', models.IntegerField()),
                ('acousticness', models.FloatField()),
                ('tempo', models.FloatField()),
                ('duration_ms', models.IntegerField()),
                ('num_sections', models.IntegerField()),
                ('num_segments', models.IntegerField()),
                ('star_rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(('star_rating__gte', 0), ('star_rating__lte', 5)), name='star_rating_value_range')],
            },
        ),
    ]
