from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from musicapp.views import ArtistViewSet, AlbumViewSet, SongViewsSet

r = DefaultRouter()
r.register('artist', ArtistViewSet)
r.register('album', AlbumViewSet)
r.register('song', SongViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls))
]