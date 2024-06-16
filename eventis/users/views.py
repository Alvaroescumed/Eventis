from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import * 
from eventos.models  import Ticket
from eventos.serializers  import TicketSerializer

# Creamos las views CRUD para user
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

class UserRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer


# Creamos otra view en la que se muestran los tikets por usuario

class UserTickets(APIView):

    def get(self, request, user_id):

        user = User.objects.get(id=user_id)
        user_ticket= Ticket.objects.filter(user=user)
        serializer = TicketSerializer(user_ticket, many=True)
        return Response(serializer.data)