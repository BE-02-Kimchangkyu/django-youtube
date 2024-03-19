from django.urls import path
from . views import (
    VideoList
)

# api/vi/video
urlpatterns = [
    path('', VideoList.as_view(), name=('video-list'))
]