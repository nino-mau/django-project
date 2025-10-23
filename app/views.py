from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from app import models, forms


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


class ImageListView(ListView):
    model = models.Image
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class CategoryImageListView(ListView):
    model = models.Image
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class ImageDetailView(DetailView):
    model = models.Image
    template_name = "image.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class ImageDeleteView(DeleteView):
    model = models.Image
    success_url = "/images"


class ImageUpdateView(UpdateView):
    model = models.Image
    template_name = "image_update.html"
    form_class = forms.UpdateImageForm
    success_url = "/images"


class ImageCreateView(CreateView):
    model = models.Image
    template_name = "image_create.html"
    form_class = forms.UploadImageForm
    success_url = "/images"
