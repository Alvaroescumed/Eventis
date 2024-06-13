from rest_framework import serializers
from .models import Concert, Festival, Event, Artist
import datetime

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

# class EventSerializer(serializers.ModelSerializer):

#     artists = ArtistSerializer(many=True)


#     def create(self, validated_data):
#         artists_data = validated_data.pop('artists', [])
#         event = Event.objects.create(**validated_data)

#         for artist_data in artists_data:
#             artist, created = Artist.objects.get_or_create(**artist_data)
#             event.artists.add(artist)

#         return event

#     def to_representation(self, instance):

#         representation = super().to_representation(instance)
#         representation['artists'] = [artist.name for artist in instance.artists.all()]
#         return representation
    
#     def validate_capacity(self, value):
#         if value < 0:
#             raise serializers.ValidationError('Capacity must be positive ')
#         return value
    
#     def validate_date(self, value):

#         today = datetime.date.today()

#         if value < today:
#             raise serializers.ValidationError('You can not create an event in the past')
#         return value
    
#     class Meta:
#         model = Event
#         fields = '__all__'

    
class ConcertSerializer(serializers.ModelSerializer):
    
    artists = ArtistSerializer(many=True)

    def create(self, validated_data):
        artists_data = validated_data.pop('artists', [])
        concert = Concert.objects.create(**validated_data)

        for artist_data in artists_data:
            artist, created = Artist.objects.get_or_create(**artist_data)
            concert.artists.add(artist)

        return concert

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['artists'] = [artist.name for artist in instance.artists.all()]
        return representation
    
    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError('Capacity must be positive ')
        return value
    
    def validate_date(self, value):

        today = datetime.date.today()

        if value < today:
            raise serializers.ValidationError('You can not create an event in the past')
        return value
    
    class Meta:
        model = Concert
        fields = '__all__'


class FestivalSerializer(serializers.ModelSerializer):

    artists = ArtistSerializer(many=True)
    
    def create(self, validated_data):
        artists_data = validated_data.pop('artists', [])
        festival = Festival.objects.create(**validated_data)

        for artist_data in artists_data:
            artist, created = Artist.objects.get_or_create(**artist_data)
            festival.artists.add(artist)

        return festival

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['artists'] = [artist.name for artist in instance.artists.all()]
        return representation
    
    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError('Capacity must be positive ')
        return value
    
    def validate_date(self, value):

        today = datetime.date.today()

        if value < today:
            raise serializers.ValidationError('You can not create an event in the past')
        return value

    class Meta:
        model = Festival
        fields = '__all__'

    
    def validate(self, data):
    
        date = data.get('date')
        end = data.get('end_date')

        if end and date and end < date:
            raise serializers.ValidationError('The festival must end after it starts')
        
        return data
        