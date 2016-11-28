from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name',
                  'phone',
                  'work_time',
                  'category',
                  'description',
                  'location',
                  'image',)


class StructuresSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Structures
        fields = ('id', 'address',
                  'index',
                  'shops')


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ('id', 'name',
                  'location')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'name',
                  'start_date',
                  'end_date',
                  'description',
                  'image')


class AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertisements
        fields = ('id', 'name', 'name', 'file', 'orientation',
                  'active',
                  'type',
                  'time',
                  'play_list',
                  )


class PlayListAdvertisingSerializer(serializers.ModelSerializer):
    play = AdvertisingSerializer(many=True, read_only=True)
    class Meta:
        model = PlayListAdvertisements
        fields = ('id', 'name', 'play')
