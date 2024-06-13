from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Concert, Artist, Festival
from .serializers import ConcertSerializer, ArtistSerializer,FestivalSerializer

class EventSearch(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_filds = ['name']

class EventOrder(generics.ListAPIView):
    filter_backends = [filters.OrderingFilter]
    search_filds = ['date']

# ----- Artist -----------

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# ----- Concerts ---------

class ConcertsListCreate(generics.ListCreateAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

class ConcertsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer

class ConcertsSearch(EventSearch):
    queryset = Concert.objects.all()
    serializer_class= ConcertSerializer

class ConcertsOrder(EventOrder):
    queryset = Concert.objects.all()
    serializer_class= ConcertSerializer

# ------ Festivals -------

class FestivalsListCreate(generics.ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

class FestivalsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer

class FestivalsSearch(EventSearch):
    queryset = Festival.objects.all()
    serializer_class= FestivalSerializer

class FestivalsOrder(EventOrder):
    queryset = Festival.objects.all()
    serializer_class= FestivalSerializer