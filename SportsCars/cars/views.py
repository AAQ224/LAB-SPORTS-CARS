from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404

# Create your views here.

cars_data = {
    1: {
        "name": "Porsche 911 Turbo S",
        "brand": "Porsche",
        "price": "1,295,000",
        "engine": "3.8L Twin-Turbo",
        "horsepower": 640,
    },
    2: {
        "name": "Ferrari F8 Tributo",
        "brand": "Ferrari",
        "price": "1,490,000",
        "engine": "3.9L Twin-Turbo V8",
        "horsepower": 710,
    },
    3: {
        "name": "Lamborghini Huracán",
        "brand": "Lamborghini",
        "price": "1,420,000",
        "engine": "5.2L V10",
        "horsepower": 631,
    },
}

def home(request):
    return render(request, "cars/home.html")


def all_cars(request):
    return render(request, "cars/all_cars.html")


def car_detail(request, car_id):
    car = cars_data.get(car_id)

    if car is None:
        raise Http404("Car not found")

    return render(request, "cars/car_detail.html", {
        "car": car
    })


def about(request):
    return render(request, "cars/about.html")
