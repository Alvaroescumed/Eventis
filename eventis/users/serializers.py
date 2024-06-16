from rest_framework import serializers
from .models import User
import datetime

#sserializamos el usuario
class userSerializer(serializers.ModelSerializer):

    #Validamos que la fecha de cumpleaños sea inferior a la fecha actual
    def validate_birth_date(self, value):
        today = datetime.date.today()

        if value > today:
            raise serializers.ValidationError('Introduzca una fecha de cumpleaños correcta')
        return value
    
    class Meta: 
        model=User
        fields = '__all__'