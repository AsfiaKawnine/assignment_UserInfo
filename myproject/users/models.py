# developed by Asfia Kawnine

from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip}"

class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Child(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"