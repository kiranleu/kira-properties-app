from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from accounts.models import Profile
from rentedproperties.models import Property
from django.contrib.auth.decorators import login_required, permission_required
from reviews.forms import ReviewForm
from .forms import PropertyForm
from django.utils import timezone


# Create your views here.
def home_page(request):
    return render(request, "rentedproperties/homepage.html")
    
def property_list(request):
    properties = Property.objects.all()
    return render(request, "rentedproperties/rented_properties_list.html", {'properties': properties})
    #return HttpResponse("Hello")

    
def property_detail(request, id):
    the_property= get_object_or_404(Property, pk=id)
    form = ReviewForm()
    return render(request, "rentedproperties/rented_properties_detail.html", {'property':the_property, 'form': form})

def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        profile = Profile.objects.create(user=request.user)

        if form.is_valid():
            new_property=form.save(commit=False)
            new_property.tenant=request.user.profile
            new_property.save()
        else:
            return HttpResponse(str(form.errors))
        
        return redirect(property_detail, new_property.id)
    else:
        form = PropertyForm()
        return render(request,"rentedproperties/add_property.html",{'form':form})


   