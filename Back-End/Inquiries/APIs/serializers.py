from rest_framework import serializers
from .models import Person, Approval


class PersonSerializer(serializers.ModelSerializer):

    committe_type = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'rank', 'approval_type', 'diagnosis',
                  'approval_date', 'additional_note', 'committe_type']

    def get_committe_type(self, obj):
        return obj.approval.committe_type


class ApprovalSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'
