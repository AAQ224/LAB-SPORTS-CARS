
from django.http import Http404
from django.shortcuts import render


cars_data = {
    1: {
        "id": 1,
        "name": "Porsche 992 GT3 R",
        "brand": "Porsche",
        "year": 2024,
        "engine": "4.2L Flat-Six",
        "horsepower": 565,
        "price": "Contact for Price",
        "model": "cars/models/2024_porsche_992_gt3_r.glb",
        "image": "cars/images/Porsche 992 GT3 R.png",
        "description": (
            "Built for the race track, the Porsche 911 GT3 R "
            "combines precision engineering, aerodynamics "
            "and uncompromising performance."
        ),
    },
    2: {
        "id": 2,
        "name": "Bugatti Tourbillon",
        "brand": "Bugatti",
        "year": 2026,
        "engine": "8.3L V16 Hybrid",
        "horsepower": 1800,
        "price": "Contact for Price",
        "model": "cars/models/2026_bugatti_tourbillon.glb",
        "image": "cars/images/Bugatti Tourbillon.png",
        "description": (
            "An extraordinary hypercar combining a naturally "
            "aspirated V16 engine with electric power "
            "and exceptional craftsmanship."
        ),
    },
    3: {
        "id": 3,
        "name": "Chevrolet Corvette C7",
        "brand": "Chevrolet",
        "year": 2014,
        "engine": "6.2L V8",
        "horsepower": 455,
        "price": "Contact for Price",
        "model": "cars/models/chevrolet_corvette_c7.glb",
        "image": "cars/images/Chevrolet Corvette C7.png",
        "description": (
            "The seventh-generation Corvette delivers "
            "an iconic American sports-car experience "
            "with aggressive styling and V8 performance."
        ),
    },
}


def home(request):
    featured_cars = list(cars_data.values())

    return render(
        request,
        "cars/home.html",
        {
            "featured_cars": featured_cars,
        },
    )


def all_cars(request):
    return render(
        request,
        "cars/all_cars.html",
        {
            "cars": list(cars_data.values()),
        },
    )


def car_detail(request, car_id):
    car = cars_data.get(car_id)

    if car is None:
        raise Http404("Car not found")

    return render(
        request,
        "cars/car_detail.html",
        {
            "car": car,
        },
    )


def about(request):
    return render(request, "cars/about.html")
