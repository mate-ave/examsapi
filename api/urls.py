from django.urls import path
from . import views

urlpatterns = [
    path('parciales/', views.ParcialesList.as_view()),
    path('parciales/<str:materia>/', views.ParcialesMateriaList.as_view()),
    path('parciales/id/<pk>', views.ParcialDetailView.as_view()),
]