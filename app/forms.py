from django import forms
from app import models


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.Images
        fields = "__all__"
