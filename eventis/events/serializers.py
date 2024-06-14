from rest_framework import serializers
from .models import Concert, Festival, Event, Artist
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
        abstract = True
        fields = '__all__'

 # usamos el serializador base para crear los diferenrtes tipos de eventos
    
class ConcertSerializer(EventSerializer):

    class Meta:
        model = Concert
        fields = '__all__'

class FestivalSerializer(EventSerializer):

    class Meta:
        model = Festival
        fields = '__all__'

    # creamos dentro de festival otro validar que nos compruebe que la ficha del final del festival sea superior a la del día que da comienzo
    def validate(self, data):
        date = data.get('date')
        end_date = data.get('end_date')

        if end_date and date and end_date < date:
            raise serializers.ValidationError('The festival must end after it starts')
        
        return data