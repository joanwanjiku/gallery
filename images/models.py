from django.db import models

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name
    
    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls, loc_id):
        loc = cls.objects.get(pk=loc_id)
        loc.delete()

    @classmethod
    def update_location(cls, loc_id, new_name):
        loc = cls.objects.filter(pk=loc_id).update(loc_name=new_name)
        return loc

class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls, cat_id):
        cat = cls.objects.get(pk=cat_id)
        cat.delete()

    @classmethod
    def update_category(cls, cat_id, new_name):
        cat = cls.objects.filter(pk=cat_id).update(cat_name=new_name)
        return cat

    

class Image(models.Model):
    image = models.ImageField(upload_to = 'all_images/', null=True)
    image_name = models.CharField(max_length=20)
    image_desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, img_id):
        image = cls.objects.get(pk=img_id)
        image.delete()

    @classmethod
    def update_image(cls, img_id, img_name, img_desc):
        image = cls.objects.filter(pk=img_id).update(image_name=img_name, image_desc=img_desc)
        return image

    @classmethod
    def search_image_by_cat(cls, cat_id):
        images = cls.objects.filter(image_cat=cat_id)
        return images
    @classmethod
    def filter_image_by_loc(cls, loc_id):
        images = cls.objects.filter(image_loc=loc_id)
        return images


