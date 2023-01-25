from rest_framework import serializers
from .models import ContactForm,Stocks



class StockSerializer (serializers.ModelSerializer):
    stock_type= serializers.CharField(max_length=100)
    stock_desc= serializers.CharField(max_length=200)
    price= serializers.IntegerField()
    quantity= serializers.IntegerField()
    class Meta:
        model = Stocks
        fields = (
            'stock_type',
            'stock_desc',
            'price',
            'quantity'
        )




class contactformSerializer(serializers.ModelSerializer):
    fname= serializers.CharField(max_length=100)
    lname= serializers.CharField(max_length=100)
    number= serializers.CharField(max_length=50)
    email= serializers.EmailField()
    password=serializers.CharField(max_length=50)
    Address= serializers.CharField(max_length=200)
    class Meta:
        model = ContactForm
        fields = (
            'fname',
            'lname',
            'number',
            'email',
            'password',
            'Address'
        )

