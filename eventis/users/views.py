from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import * 
from eventos.models  import Assistants
from eventos.serializers  import AssistantSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

class UserRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

class UserTickets(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    def get(self, req):

        user = req.user
        user_ticket= Assistants.objects.filter(user=user)
        serializer = AssistantSerializer(user_ticket, many=True)
        return Response(serializer.data)