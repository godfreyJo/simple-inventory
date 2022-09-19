from django.urls import path
from . import views

urlspatterns = [
    path('', views.ExpenseListAPIView(), name='expenses'),
    path('<int:id>', views.ExpenseListAPIView(), name='detailed-expenses'),
]