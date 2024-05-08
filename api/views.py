from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PDFFileSerializer, PhotoSerializer
from .models import Photo, PDFFile
from rest_framework import generics


class PDFFileAPIView(generics.ListCreateAPIView):
    queryset = PDFFile.objects.all()
    serializer_class = PDFFileSerializer


class PhotoAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_class = [MultiPartParser, FormParser]