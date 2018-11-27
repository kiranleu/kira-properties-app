from django.shortcuts import render, redirect
from .forms import ReviewForm
from rentedproperties.models import Property

def write_review(request, id):
    form = ReviewForm(request.POST)
    review = form.save(commit=False)
    properties = get_object_or_404(Property, pk=id)
    review.property_id = id
    review.author = request.user
    review.save()
    return redirect("property_detail", {'properties': properties}) 