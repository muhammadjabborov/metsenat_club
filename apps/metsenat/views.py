from django.shortcuts import render
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import models
from .models import Sponsor, Student, University, StudentSponsor
from metsenat import serializers

class DashboardData(ListAPIView):
    serializer_class = serializers.UpdateStudentSponsorSerializer

    def get(self, request, format=None):
        total_spent = Sponsor.objects.aggregate(total_sponsors_spent=models.Sum('spent_amount'))
        total_tuition_fee = Student.objects.aggregate(total_tuition_fee=models.Sum('tuition_fee'))

        total_spent = total_spent['total_sponsors_spent']
        total_tuition_fee = total_tuition_fee['total_tuition_fee']

        required_amount = total_tuition_fee - total_spent

        return Response({'total_sponsors_spent': total_spent,
                         'total_tuition_fee': total_tuition_fee,
                         'required_amount': required_amount})


class DashboardLineStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.LineDashboardStudentsSerializer


class DashboardLineSponsor(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.LineDashboardSponsorsSerializer


class CreateSponsorView(ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.CreateSponsorSerializer

    permission_classes = [IsAuthenticated]


class ListSponsorsView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.ListSponsorsSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('status', 'balance')
    search_fields = ('name',)


class DetailSponsorView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.DetailSponsorSerializer

    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


class UpdateSponsorView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.UpdateSponsorSerializer

    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


class CreateUniversityView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = serializers.CreateUniversitySerializer

    permission_classes = (IsAuthenticated,)


class CreateStudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.CreateStudentSerializer

    permission_classes = (IsAuthenticated,)


class ListStudentsView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.ListStudentsSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('student_type', 'university')
    search_fields = ('name',)


class DetailStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.DetailStudentSerializer

    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


class UpdateStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.UpdateStudentSerializer

    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset


class CreateStudentSponsorView(CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = serializers.StudentSponsorSerializer
    permission_classes = (IsAuthenticated,)


class UpdateStudentSponsorView(RetrieveUpdateDestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = serializers.UpdateStudentSponsorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('id', None):
            queryset = queryset.filter(id=self.kwargs['id'])

        return queryset
