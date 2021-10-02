# developed by Asfia Kawnine

from rest_framework import viewsets

from .serializers import *
from .models import *


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all().order_by('created_date')
    serializer_class = AddressSerializer


class ParentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Parent.objects.all().order_by('created_date')
    serializer_class = ParentSerializer


class ChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Child.objects.all().order_by('created_date')
    serializer_class = ChildSerializer