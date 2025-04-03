from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CompanySerializer, VacancySerializer

from api.models import Company, Vacancy

class EntityListView(APIView):
    def get(self, request, entity_type=None):
        if entity_type == 'companies':
            try:
                companies = Company.objects.all()
                serializer = CompanySerializer(companies, many=True)
                return Response(serializer.data)
            except Company.DoesNotExist as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        elif entity_type == 'vacancies':
            try:
                vacancies = Vacancy.objects.all()
                serializer = VacancySerializer(vacancies, many=True)
                return Response(serializer.data)
            except Vacancy.DoesNotExist:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Invalid entity type."}, status=status.HTTP_400_BAD_REQUEST)
        
class SearchByIdAPIView(APIView):
    def get(self, request, id, entity_type=None):
        if entity_type == 'companies':
            try:
                company = Company.objects.get(id=id)
                serializer = CompanySerializer(company)
                return Response(serializer.data)
            except Company.DoesNotExist:
                return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        elif entity_type == 'vacancies':
            try:
                vacancy = Vacancy.objects.get(id=id)
                serializer = VacancySerializer(vacancy)
                return Response(serializer.data)
            except Vacancy.DoesNotExist:
                return Response({"detail": "Vacancy not found."}, status=status.HTTP_404_NOT_FOUND)
                
        else:
            return Response({"detail": "Invalid entity type."}, status=status.HTTP_400_BAD_REQUEST)
        
class CompanyVacanciesView(APIView):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response({"detail": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
        
class Top10VacanciesAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
