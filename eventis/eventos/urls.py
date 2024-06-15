from django.urls import path
from .views import *

urlpatterns = [
    path('artists/', ArtistListCreate.as_view(), name='artist_list_create'),
    path('artists/<int:pk>', ArtistRetriveUpdateDestroy.as_view(), name='arists_rud'),
    path('', EventsListCreate.as_view(), name='event_list'),
    path('<str:name>', ArtisEventsList.as_view(), name='artist_events_list'),
    path('<str:location>', EventsLocationList.as_view(), name='locations_vents_list'),
    path('attend/', AddAssitance.as_view(), name='attend_event'),
    path('assistants/<int:event_id>', EventAttendeesList.as_view(), name='list_assistants' )
]