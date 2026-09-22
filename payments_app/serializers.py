from rest_framework import serializers
# pyrefly: ignore [missing-import]
from .models import PaymentTransaction

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'
        read_only_fields = ('status', 'transaction_id')
