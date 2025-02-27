import json
from song_playlist_api.models import Song
import logging

logger = logging.getLogger(__name__)

def upload_playlist_service(file):
    
    data = file.read()
    print(type(data))
    print()
    
    # for i in range(len(data['id'])):
    #     song = Song(
    #         id=data['id'][str(i)],
    #         title=data['title'][str(i)],
    #         danceability=data['danceability'][str(i)],
    #         energy=data['energy'][str(i)],
    #         mode=data['mode'][str(i)],
    #         acousticness=data['acousticness'][str(i)],
    #         tempo=data['tempo'][str(i)],
    #         duration_ms=data['duration_ms'][str(i)],
    #         num_sections=data['num_sections'][str(i)],
    #         num_segments=data['num_segments'][str(i)],
    #     )

    #     logger.info(f"Saving song with id: {data['id'][str(i)]}")
    #     song.save()
    #     logger.info(f"Saved song with id: {data['id'][str(i)]}")