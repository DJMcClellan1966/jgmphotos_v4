from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView, ListView, FormView, View

from .models import Image
from . import views

class GalleryListView(ListView):
    model = Image
    template_name = "photos/gallery.html"

    def get_queryset(self):
        # Order by newest first
        return super(GalleryListView, self).get_queryset().order_by('-pk')
