from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer


# Create your views here.


class ExpenseList(ListCreateAPIView):
    serializer_class = ExpenseSerializer