from django.urls import path, re_path
from .views import home  # import the view
from .views import SongListView, SongDetailView, SongUpdateView, SongDeleteView, SongCreateView  # import the class-based views

urlpatterns = [
    # path('', home, name='home'),  # connect the view to a URL
    path('', SongListView.as_view(), name='song_list'),
    path('<int:song_Number>/<slug:slug>', SongDetailView.as_view(), name='song_detail'),
    # re_path(r'^songs/(?P<song_Number>[0-9]+)/(?P<slug>[\w-]+)/$', SongDetailView.as_view(), name='song_detail'),
    path('<int:song_Number>/<slug:slug>/edit', SongUpdateView.as_view(), name='song_update'),
    path('new/', SongCreateView.as_view(), name='song_create'),
    path('<int:song_Number>/<slug:slug>/delete', SongDeleteView.as_view(), name='song_delete'),

]
