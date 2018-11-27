from django.contrib import admin
from rentedproperties.models import Property, Landlord, Tenant

# Register your models here.
admin.site.register(Property)
admin.site.register(Landlord)
admin.site.register(Tenant)
