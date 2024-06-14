from django.urls import path
from .views import *

urlpatterns= [
    path('concerts/', ConcertsListCreate.as_view(), name='concerts_list_create'),
    path('artists/', ArtistListCreate.as_view(), name='artist_list_create'),
    path('festivals/', FestivalsListCreate.as_view(), name='festivals-list-create'),
    path('artists/<int:pk>', ArtistRetriveUpdateDestroy.as_view(), name='arists_rud'),
    path('concerts/<int:pk>', ConcertsRetriveUpdateDestroy.as_view(), name='concerts_rud'),
    path('festivals/<int:pk>', FestivalsRetriveUpdateDestroy.as_view(), name='festivals-rud'),
    path('concerts/search/', ConcertsSearch.as_view(), name='concerts_search'),
    path('events/', EventsList.as_view(), name='event_list'),
    path('events/<str:name>', ArtisEventsList.as_view(), name='artist-events-list'),
    path('events/<str:location>', EventsLocationList.as_view(), name='locations-events-list')
]