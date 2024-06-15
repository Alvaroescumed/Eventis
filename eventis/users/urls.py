from django.urls import path
from .views import * 

urlpatterns = [
    path('', UserListCreate.as_view(), name='user_list_create'),
    path('<int:pk>', UserRetriveUpdateDestroy.as_view(), name='user_rud'),
    path('tickets/', UserTickets.as_view(), name='user_tickets')
]