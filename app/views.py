from django.utils import timezone
from django.views.generic import DetailView, ListView

from app import models


class ImagesListView(ListView):
    model = models.Images
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class ImageDetailView(DetailView):
    model = models.Images
    template_name = "image.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
