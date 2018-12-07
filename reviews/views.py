from django.shortcuts import render, redirect
from rentedproperties.views import property_detail
from .forms import ReviewForm
from rentedproperties.models import Property

def write_review(request, id):
    form = ReviewForm(request.POST)
    review = form.save(commit=False)
    review.the_property_id = id
    review.profile_id = request.user
    review.save()
    return redirect('property_detail', id=id)