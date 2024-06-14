from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

 
# ----- Artist -----------

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# ----- Concerts ---------

class EventsListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# ---- API Views ------
    
class EventsLocationList(APIView):

    # traemos por parametro la localizacion en la que queremos filtar los eventos
    def get(self, req, location): 

        events = Event.objects.filter(events__location__icontains = location)

        events_serializer = EventSerializer(events, many=True)
        response_data = events_serializer.data  

        #En caso de que no haya un evento en la ciudad deseada nos mostrara un mensaje avisando al usuario
        if not response_data:
            response_data = 'Por ahora no hay enventos aquí :('
            
        return Response ({f"Eventos en {location}": response_data})
    
class ArtisEventsList(APIView):
    
    # tomamos la misma mecanica que en la anterior view cambiando la localizacion por el artista deseado
    def get(self, req, name): 

        events = Event.objects.filter(artists__name__icontains = name)

        events_serializer = EventSerializer(events, many=True)
        response_data = events_serializer.data

        if not  response_data:
            response_data = 'Por ahora este artista no tiene eventos :('

        return Response ({f"{name} eventos": response_data})
    
# Creamos la view para la compra de entradas

