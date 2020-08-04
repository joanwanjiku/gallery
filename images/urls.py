from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('search/', views.image_results, name='image_results'),
    path('location/<int:loc_id>', views.image_location, name='image_location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
