from rest_framework import serializers
from messmenu.models import MenuDetails
from messmenu.models import Hostel
class HostelSerializer(serializers.ModelSerializer):
	"""Serializer for the hostel model"""
	WeeklyMenu = MenuDetailsSerializer(many=True)
	class Meta:
		model = Hostel
		fields = ('hostel')
class MenuDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuDetails
		fields = '__all__'