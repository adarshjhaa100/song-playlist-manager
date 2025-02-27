from django.db import models
from django.db.models import CheckConstraint, Q

class Song(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    danceability = models.FloatField()
    energy = models.FloatField()
    mode = models.IntegerField()
    acousticness = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    star_rating = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(star_rating__gte=0) & Q(star_rating__lte=5), name='star_rating_value_range'
            )
        ]
        app_label = 'song_playlist_api'

    def __str__(self):
        return self.title
    
    @staticmethod
    def ignore_fields():
        return ['star_rating']
    
    @staticmethod
    def input_fields():
        return [ x for x in Song._meta.get_fields() if x not in Song.ignore_fields() ]