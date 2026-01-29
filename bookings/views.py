from django.shortcuts import render
from .models import Bookings

# Create your views here.

def book_table(request):
    if request.method == "POST":
        # handle form submission
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        guests = request.POST.get('guests')
        date = request.POST.get('date')
        message = request.POST.get('message')

        # save to database
        Bookings.objects.create(
            Name=name,
            Phone=phone,
            No_of_people=guests,
            Date=date,
            Message=message
        )
        print(request.POST)

    return render(request, 'booktable.html')

def index(request):
    return render(request, 'index.html')


