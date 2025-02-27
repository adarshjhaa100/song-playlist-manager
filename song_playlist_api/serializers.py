from rest_framework import serializers
import json
from .models import Song
import logging

logger = logging.getLogger(__name__)

class UploadedSongSerializer(serializers.Serializer):
    file = serializers.FileField()

    def to_internal_value(self, data):
        file = data.get('file')

        if not file:
            raise serializers.ValidationError({"file": "This field is required."})

        try:
            file_content = file.read().decode('utf-8')
            data = json.loads(file_content)
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise serializers.ValidationError({"file": "Invalid JSON file."})
        except Exception as e:
            raise serializers.ValidationError({"file": f"Error reading file: {str(e)}"})

        songs = []
        print(len(data["id"].keys()), Song.input_fields())
        playlist_size = len(data["id"].keys())

        logger.info(f"processing for playlist size: {playlist_size}")
    
        for i in range(playlist_size):
            song_data = {}
            
            for field in Song.input_fields():
                colname =field.column
                # print(colname)
                try:
                    song_data[colname] = data[colname][str(i)] if colname in data else None
                except:
                    pass
            songs.append(song_data)    
            logger.debug(f"Song serialized {song_data['id']}")            
        return songs

    def create(self, validated_data):
        song_serializer = SongSerializer(data=validated_data, many=True)
        if song_serializer.is_valid():
            song_serializer.save()
            return song_serializer.data
        else:
            raise serializers.ValidationError(song_serializer.errors)

    def update(self, instance, validated_data):
        raise NotImplementedError("Update operation is not supported.")

    def to_representation(self, instance):
       return instance

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
