from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class UserLandSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',  'email')

class FarmerSerializer(serializers.ModelSerializer):
    user = UserLandSerializer(read_only=True)
    class Meta:
        model = Farmer
        fields = '__all__'  # Tüm alanları dahil et

class PartnerSerializer(serializers.ModelSerializer):
    user = UserLandSerializer(read_only=True)
    class Meta:
        model = Partner
        fields = '__all__'  # Tüm alanları dahil et




class LandSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(read_only=True)
    partner = PartnerSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    neighborhood = NeighborhoodSerializer(read_only=True)
    street = StreetSerializer(read_only=True)

    class Meta:
        model = Land
        fields = '__all__'


class LandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandDetail
        fields = '__all__'  # Tüm alanları dahil et

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'  # Tüm alanları dahil et

class WeatherAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherAlert
        fields = '__all__'  # Tüm alanları dahil et

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user