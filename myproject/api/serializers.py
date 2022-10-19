from asyncore import read
from rest_framework import serializers
from base.models import Culture,Person,Serre 

#serrreeee

class SerreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serre
        fields = '__all__'
  
class CultSerializer(serializers.ModelSerializer):
    serrekult = SerreSerializer(read_only=True,many=True)
    class Meta:
        model = Culture
        fields = '__all__'

class PersSerializer(serializers.ModelSerializer):
    serrepers = SerreSerializer(read_only=True,many=True)
    class Meta:
        model = Person
        fields = '__all__'
      