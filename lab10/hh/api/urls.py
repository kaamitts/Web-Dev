from django.urls import path
from api.views.companyViewsCBV import CompanyListView, CompanyDetailView, CompanyVacanciesView
from api.views.vacancyViewsFBV import vacancy_list, vacancy_detail, top_10_vacancies

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='List of campanies'),
    path('companies/<int:id>/', CompanyDetailView.as_view(), name = 'Company datails'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesView.as_view(), name='vacancy in the company'),
    path('vacancies/', vacancy_list, name = 'List of vacancies'),
    path('vacancies/<int:id>', vacancy_detail, name = 'Vacancy Datial'),
    path('vacancies/top_ten/', top_10_vacancies, name='top-ten-vacancies'),
]