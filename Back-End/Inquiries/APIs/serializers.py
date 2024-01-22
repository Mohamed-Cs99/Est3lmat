from rest_framework import serializers
from .models import Person, Approval


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ApprovalSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'
