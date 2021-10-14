from rest_framework import serializers
from .models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Request
        fields = ["user", "server", "location",
                  "contact_person", "contact_number", "date", "status"]

    def create(self, validated_data):
        request, created = Request.objects.update_or_create(
            user=validated_data.get('user'),
            defaults={'user': validated_data.get('user'), 'server': validated_data.get('server'),
                      'location': validated_data.get('location'), 'contact_person': validated_data.get('contact_person'), 'contact_number': validated_data.get('contact_number'), 'date': validated_data.get('date'), 'status': validated_data.get('status')})
        return request
