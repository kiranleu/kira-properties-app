from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from rentedproperties.models import Property, Landlord, Tenant
from reviews.forms import ReviewForm



# Create your views here.
def property_list(request):
    properties = Property.objects.all()
    return render(request, "rentedproperties/rented_properties_list.html", {'properties': properties})
    #return HttpResponse("Hello")

    
def property_detail(request, id):
    the_property= get_object_or_404(Property, pk=id)
    form = ReviewForm()
    return render(request, "rentedproperties/rented_properties_detail.html", {'property':the_property, 'form': form})


