# developed by Asfia Kawnine

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


from .models import *


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'zip']


class ParentSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    address = AddressSerializer()
    
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'address']

    def to_representation(self, instance):
        self.fields['address'] =  AddressSerializer(read_only=True)
        return super(ParentSerializer, self).to_representation(instance)


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'parent']

    def to_representation(self, instance):
        self.fields['parent'] =  ParentSerializer(read_only=True)
        return super(ChildSerializer, self).to_representation(instance)