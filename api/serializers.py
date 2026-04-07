from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'date', 'capacity', 'organizer', 'categories']