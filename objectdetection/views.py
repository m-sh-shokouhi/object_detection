from django.shortcuts import render


def home(request):
    return render(request, template_name="objectdetection/home.html")


def about_us(request):
    return render(request, template_name="objectdetection/about_us.html")


def contact_us(request):
    return render(request, template_name="objectdetection/contact_us.html")
