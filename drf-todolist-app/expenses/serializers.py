from rest_framework import serializers



class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Expense
        fields=['date','category','description','amount']
