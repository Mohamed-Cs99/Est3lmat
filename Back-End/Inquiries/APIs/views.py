from django.shortcuts import render
from rest_framework import generics
from .models import Person, Approval
from .serializers import PersonSerializer, ApprovalSerailzer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class PersonView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]


class SinglePersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]


class ApprovalView(generics.ListCreateAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerailzer
    permission_classes = [IsAuthenticated]


class SingleApprovalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerailzer
    permission_classes = [IsAuthenticated]
