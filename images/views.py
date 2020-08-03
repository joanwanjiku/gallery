from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    return render(request, 'index.html', {'title':title, 'images': images})