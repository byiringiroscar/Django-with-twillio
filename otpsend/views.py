from django.shortcuts import render
from .models import Car_registration, Tax, Control, Insurance

# Create your views here.

plate_number = 'RAD911G'


def check(request):

    return render(request, 'html/index.html')


def capture_plate(request):
    context = {
        'insurance': Insurance.objects.all(),
        'tax': Tax.objects.all(),
        'control': Control.objects.all(),
        'cars': Car_registration.objects.all(),
        'search': Car_registration.objects.all().get(plate_number=plate_number),
        'plate_number': plate_number,

    }
    return render(request, 'html/dashboard.html')
