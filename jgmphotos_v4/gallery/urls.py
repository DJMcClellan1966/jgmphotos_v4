from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from gallery.views import GalleryListView

urlpatterns = [
    path('', GalleryListView.as_view(), name = 'gallery'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
