from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RentalReview

# Create your views here.
def rental_review(request):
    if request.method == 'POST':
        my_form = RentalReview(request.POST)

        if my_form.is_valid():
            print(my_form.cleaned_data)
            return redirect(reverse('rentals:thank_you'))
    else:
        my_form = RentalReview()
        return render(request, 'rentals/rental_review.html', context = { 'form': my_form})


def thank_you(request):
    return render(request, 'rentals/thank_you.html')