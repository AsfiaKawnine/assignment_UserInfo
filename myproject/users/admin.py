# developed by Asfia Kawnine

from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import *


admin.site.register(Address)
admin.site.register(Parent)
admin.site.register(Child)

admin.site.unregister(User)
admin.site.unregister(Group)
