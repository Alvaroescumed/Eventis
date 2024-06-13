from django.urls import path
from .views import *

urlpatterns= [
    path('concerts/', ConcertsListCreate.as_view(), name='concerts_list_create'),
    path('artists/', ArtistListCreate.as_view(), name='artist_list_create'),
    path('festivals/', FestivalsListCreate.as_view(), name='festivals-list-create'),
    path('artists/<int:pk>', ArtistRetriveUpdateDestroy.as_view(), name='arists_rud'),
    path('concerts/<int:pk>', ConcertsRetriveUpdateDestroy.as_view(), name='concerts_rud'),
    path('concerts/search/', ConcertsSearch.as_view(), name='concerts_search'),
]