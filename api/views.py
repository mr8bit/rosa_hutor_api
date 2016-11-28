from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class StructuresViewSet(viewsets.ModelViewSet):
    serializer_class = StructuresSerializer
    queryset = Structures.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'structures': serializer.data})


class TerminalViewSet(viewsets.ModelViewSet):
    serializer_class = TerminalSerializer
    queryset = Terminal.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'terminal': serializer.data})


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'events': serializer.data})


class PlayListAdvertisingViewSet(viewsets.ModelViewSet):
    serializer_class = PlayListAdvertisingSerializer
    queryset = PlayListAdvertisements.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'play_list_advertisements': serializer.data})

