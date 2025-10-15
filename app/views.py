from django.shortcuts import render


def index(request):
    context = {}
    context["name"] = "toto"
    return render(request, "index.html", context)
