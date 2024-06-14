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

# ---- API Views --------

class EventsList(APIView):

    def get(self, req):
        concerts = Concert.objects.all()
        festivals = Festival.objects.all()

        concerts_serializer = ConcertSerializer(concerts, many=True)
        festivals_serializer = FestivalSerializer(festivals,many=True)

        response_data = concerts_serializer.data + festivals_serializer.data

        return Response(response_data)
    
class EventsLocationList(APIView):

    # traemos por parametro la localizacion en la que queremos filtar los eventos
    def get(self, req, location): 

        concerts = Concert.objects.filter(location__icontains = location)
        festivals = Festival.objects.filter(artists__name__icontains = location)

        concerts_serializer = ConcertSerializer(concerts, many=True)
        festivals_serializer = FestivalSerializer(festivals, many=True)      


        response_data = concerts_serializer.data + festivals_serializer.data

        #En caso de que no haya un evento en la ciudad deseada nos mostrara un mensaje avisando al usuario
        if not response_data:
            response_data = 'Por ahora no hay enventos aquí :('
            
        return Response ({f"Eventos en {location}": response_data})
    
class ArtisEventsList(APIView):
    
    # tomamos la misma mecanica que en la anterior view cambiando la localizacion por el artista deseado
    def get(self, req, name): 

        concerts = Concert.objects.filter(artists__name__icontains = name)
        festivals = Festival.objects.filter(artists__name__icontains = name)

        concerts_serializer = ConcertSerializer(concerts, many=True)
        festivals_serializer = FestivalSerializer(festivals, many=True)      

        response_data = concerts_serializer.data + festivals_serializer.data
        if not response_data:
            response_data = 'Por ahora este artista no tiene eventos :('

        return Response ({f"{name} eventos": response_data})