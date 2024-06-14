from django.urls import path
from .views import *

urlpatterns = [
    path('artists/', ArtistListCreate.as_view(), name='artist_list_create'),
    path('artists/<int:pk>', ArtistRetriveUpdateDestroy.as_view(), name='arists_rud'),
    path('events/', EventsListCreate.as_view(), name='event_list'),
    path('events/<str:name>', ArtisEventsList.as_view(), name='artist-events-list'),
    path('events/<str:location>', EventsLocationList.as_view(), name='locations-events-list'),
    path('events/attend/', AddAssitance.as_view(), name='attend-event'),
    path('events/assistants/<int:pk>', EventAttendeesList.as_view(), name='list-assistants' )
]