from django.shortcuts import render
import os

from app import settings
from django.http import FileResponse


def index(request):
    context = {}
    context["name"] = "toto"

    return render(request, "index.html", context)


def images(request):
    context = {}

    path = settings.BASE_DIR / "app/static/images"

    image_names = os.listdir(path)

    images = []

    for name in image_names:
        image = {
            "name": name,
            "path": "/static/images/" + name,
        }
        images.append(image)

    context["images"] = images

    return render(request, "images.html", context)


def image(request, name):
    context = {}
    context["image"] = {"path": f"/static/images/{name}"}

    return render(request, "image.html", context)


def image_raw(request, name):
    file_path = settings.BASE_DIR / f"app/static/images/{name}"
    return FileResponse(open(file_path, "rb"))
