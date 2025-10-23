from django import forms
from django.forms.widgets import Input
from app import models


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.Images
        fields = "__all__"
