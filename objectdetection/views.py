from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def home(request):
<<<<<<< HEAD
    if request.method == 'POST':
        file = request.FILES['file']
        path = default_storage.save(
            'tmp/image.jpeg', ContentFile(file.read()))

        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print(tmp_file)
=======
>>>>>>> fb2c9d8181bbf6739eaa10d6bccd9cc7394ece70
    return render(request, template_name="objectdetection/home.html")


def about_us(request):
    return render(request, template_name="objectdetection/about_us.html")


def contact_us(request):
    return render(request, template_name="objectdetection/contact_us.html")
