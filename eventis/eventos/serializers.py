from rest_framework import serializers
from .models import *
import datetime

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

# creamos un serializador base para los eventos
class EventSerializer(serializers.ModelSerializer):

    #nos traemos el serializador de artistas ya que esta tabla esta relacionada con los diferentes eventos
    artists = ArtistSerializer(many=True)

    # definimos una funcion create que al serializar un nuevo evento busca si el artista ya existe en nuestra BD si no, lo crea
    def create(self, validated_data):
        artists_data = validated_data.pop('artists', [])
        event = self.Meta.model.objects.create(**validated_data)

        for artist_data in artists_data:
            artist, created = Artist.objects.get_or_create(**artist_data)
            event.artists.add(artist)

        return event

    # definimos una función para que cuando se hagan peticiones gets a los eventos los artistas aparezcan con su nombre y no con ID
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['artists'] = [artist.name for artist in instance.artists.all()]
        return representation

    # establecemos diferentes validaciones una para la capacidad del evento y otra para la fecha
    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError('Capacity must be positive')
        return value

    def validate_date(self, value):
        today = datetime.date.today()
        if value < today:
            raise serializers.ValidationError('You cannot create an event in the past')
        return value

    class Meta:
        model = Event
        fields = '__all__'

    
class AssistantSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField()
    event_name = serializers.SerializerMethodField()
    class Meta:
        model = Assistants
        fields = ['id', 'user_name', 'event_name']
    
    def get_user_name(self, obj):
        return f'{obj.user.name} {obj.user.lastname}'

    def get_event_name(self, obj):
        return obj.event.name 