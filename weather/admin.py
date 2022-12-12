from django.contrib import admin

# Register your models here.
from .models import Data,Contact,CSV

admin.site.register(Data)
admin.site.register(Contact)
admin.site.register(CSV)