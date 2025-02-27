from rest_framework import generics, status
from song_playlist_api.services.upload_playlist_service import upload_playlist_service
from .models import Song
from .serializers import SongSerializer, UploadedSongSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
import json
import logging

logger = logging.getLogger(__name__)


class SongPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongPagination
    http_method_names = ["get","post"]

class SongDetail(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'title'

class UploadSongView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    http_method_names = ["post"]
    def post(self, request):
        print(request)
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # upload_playlist_service(file)
            serializer = UploadedSongSerializer(data=request.FILES) 
            if serializer.is_valid():
                # print(f"serializer data: {serializer.validated_data}")
                song_data = serializer.create(serializer.validated_data)  # Pass validated data to create
                return Response(len(song_data), status=status.HTTP_201_CREATED)
            return Response({"message": "JSON data uploaded successfully"}, status=status.HTTP_201_CREATED)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON file"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)