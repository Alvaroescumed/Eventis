from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .serializers import *
from users.models import User


 
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

        events = Event.objects.filter(location = location)

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

class AddTicket(APIView):

    #endpoint para inscribirse al evento
    def post(self, request):

        event_id = request.query_params.get('event_id')
        user_mail = request.query_params.get('user_mail')

        print(f"id:{event_id} and {user_mail}")

        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Este evento no existe...'})
        
        try:
            user = User.objects.get(mail=user_mail)
        except Event.DoesNotExist:
            return Response({'error': 'Este usuario no existe...'})
        
        #Revisamos el aforo que tiene el evento
        current_tickets = Ticket.objects.filter(event=event).count()
        if current_tickets >= event.capacity:
            return Response({'error': 'El aforo está completo...'})

        self.send_email_notification(user.mail, user.name, event.name, event.location, event.date)
        return Response({'message': f'Has confirmado tu asistencia al evento {event.name}'})

        
    def send_email_notification(self, user_mail, user_name, event_name, event_location, event_date):
            subject = 'Confirmación de Asistencia'
            message = f' Hola {user_name}! \n\nHas confirmado tu asistencia al evento {event_name} en {event_location} para el día {event_date}. \n\nEsperamos que disfrutems mucho del concierto!, \nEl equipo de eventis'
            sender_email = settings.EMAIL_HOST_USER
            recipient_list = [user_mail]

            send_mail(subject, message, sender_email, recipient_list)

#lista de asistentes para el evento
class EventAttendeesList(APIView):
    
    def get(self, req, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Evento no encontrado'})

        tickets = Ticket.objects.filter(event=event)
        serializer = TicketSerializer(tickets, many=True)

        data = { 
            'CONCERT/FESTIVAL': event.name,
            'ASISTENTES' : serializer.data
        }
        return Response(data)