from django.test import TestCase
from .models import Category, Location, Image
# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category= Category(cat_name = 'art')
    # Testing  instance

    def tearDown(self):
        Category.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        test_category = Category(cat_name='paintings')
        test_category.save_category()
        self.category.delete_category(pk=test_category.id)

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location= Location(loc_name = 'kenya')
    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        test_location = Location(loc_name='uganda')
        test_location.save_location()
        test_location.delete_location(pk=test_location.id)

class ImageTestCase(TestCase):
    def setUp(self):
        self.location= Location(loc_name = 'kenya')
        self.category= Category(cat_name = 'art')
        self.location.save_location()
        self.category.save_category()

        self.image = Image(image='all_images/sun.jpg', image_name='sun', image_desc='beautiful sun', image_loc=self.location, image_cat=self.category)
        
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    
