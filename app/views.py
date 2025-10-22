from django.utils import timezone
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView

from app import models, forms


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


def handle_upload(request):
    form = forms.UploadImageForm()
    if request.method == "POST":
        form = forms.UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, "image_upload.html", context={"form": form})
