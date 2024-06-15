from rest_framework import serializers
from .models import User
import datetime

class userSerializer(serializers.ModelSerializer):

    def validate_birth_date(self, value):
        today = datetime.date.today()

        if value > today:
            raise serializers.ValidationError('Introduzca una fecha de cumpleaños correcta')
        return value
    
    class Meta: 
        model=User
        fields = '__all__'