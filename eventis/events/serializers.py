from rest_framework import serializers
from .models import Concert, Festival, Event, Artist
import datetime

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError('Capacity must be positive ')
        return value
    
    def validate_date(self, value):

        today = datetime.date.today()

        if value < today:
            raise serializers.ValidationError('You can not create an event in the past')
        return value
    
class ConcertSerializer(EventSerializer):
    class Meta:
        model = Concert
        fields = '__all__'


class FestivalSerializer(EventSerializer):
    class Meta:
        model = Festival
        fields = '__all__'

    
    def validate(self, data):
    
        date = data.get('date')
        end = data.get('end_date')

        if end and date and end < date:
            raise serializers.ValidationError('The festival must end after it starts')