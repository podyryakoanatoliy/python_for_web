from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def business(request):
    return render(request, "business_eng.html")


def business_ua(request):
    return render(request, "business_ru.html")


def creative(request):
    return render(request, "creative_eng.html")


def creative_ua(request):
    return render(request, "creative_ru.html")