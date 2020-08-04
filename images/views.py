from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    locations = Location.get_all_locations()
    return render(request, 'index.html', {'title':title, 'images': images, 'locations':locations})

def image_results(request):
    if 'category' in  request.GET and request.GET['category']:
        search_term = request.GET.get("category")
        category = Category.find_cat_id(search_term)
        print(category[0].id)
        searched_images = Image.search_image_by_cat(category[0].id)
        message = f"{search_term}"

        return render(request, 'category.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html',{"message":message})

def image_location(request, loc_id):
    loc_name = Location.objects.filter(pk=loc_id)[0]
    images = Image.filter_image_by_loc(loc_id)
    locations = Location.get_all_locations()

    return render(request, 'location.html', {'images': images, 'loc_name':loc_name, 'locations': locations})

