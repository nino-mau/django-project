from django import forms
from django.forms.widgets import Input
from app import models


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = "__all__"


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ["name"]
