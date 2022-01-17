from django.urls import path
from . views import *

urlpatterns = [
    path('geomatic/software',software,name='software'),
    path('geomatic/videos',video,name='video'),
    path('uploadfiles',upload,name='upload'),
    path('geomatic',level_100,name='level_100'),
]