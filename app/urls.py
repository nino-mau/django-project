"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from app import settings, views
from app.views import ImageDeleteView, ImagesListView, ImageDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("images/", ImagesListView.as_view(), name="images"),
    path("<int:pk>/", ImageDetailView.as_view(), name="image"),
    path("<int:pk>/delete", ImageDeleteView.as_view(), name="image_delete"),
    path("image_upload/", views.handle_upload, name="image_upload"),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
