from django.shortcuts import render
from .permissions import IsOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from.models import Expense
from rest_framework import permissions



# Create your views here.


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permissions = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return self.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permissions = (permissions.IsAuthenticated, IsOwner,)
    lookup_field="id"

    def perform_create(self, serializer):
        return self.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)