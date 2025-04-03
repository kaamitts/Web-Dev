from django.urls import path
from .views import EntityListView, SearchByIdAPIView, Top10VacanciesAPIView, CompanyVacanciesView

urlpatterns = [
    path('<str:entity_type>/', EntityListView.as_view(), name='entity-list'),
    path('<str:entity_type>/<int:id>/', SearchByIdAPIView.as_view(), name='entity-detail'),
    path('vacancies/top_ten/', Top10VacanciesAPIView.as_view(), name='top-ten-vacancies'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesView.as_view(), name='vacancy in the company')
]
