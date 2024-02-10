from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Song

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

class SongListView(ListView):
    model = Song
    template_name = 'songs/song_list.html'
    context_object_name = 'songs'
    paginate_by = 50


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('slug')
        search_term = self.request.GET.get('search', '')
        if search_term:

            if search_term.isdigit():
                queryset = queryset.filter(
                    Q(song_Number__exact=search_term)
                )
            else:
                queryset = queryset.filter(
                    Q(title__icontains=search_term) |
                    Q(body__icontains=search_term) |
                    Q(slug__icontains=search_term)
                )

            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(song_Number__icontains=search_term) |
                Q(body__icontains=search_term) |
                Q(slug__icontains=search_term)
            )
        return queryset

class SongDetailView(DetailView):
    model = Song
    template_name = 'songs/song_detail.html'
    context_object_name = 'song'

    def get_object(self):
        song_Number = self.kwargs.get("song_Number")
        slug = self.kwargs.get("slug")

        post = get_object_or_404(Song, song_Number=song_Number, slug=slug)
        return post

class SongUpdateView(UpdateView):
    model = Song
    fields = '__all__'
    template_name = 'songs/song_update.html'

class SongDeleteView(DeleteView):
    model = Song
    template_name = 'songs/song_delete.html'
    success_url = '/songs/'

class SongCreateView(CreateView):
    model = Song
    fields = '__all__'
    template_name = 'songs/song_create.html'
    success_url = '/songs/'