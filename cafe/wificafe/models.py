from django.db import models

class CafeBlock(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=255)
    site_url = models.URLField(max_length=500,blank=True,null=True)
    photo = models.ImageField(upload_to='cafe_photos/',blank=True,null=True)
    full_description = models.TextField(blank=True,null=True)
    google_map_embed = models.TextField(blank=True, null=True)
    total_reviews = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    cafe = models.ForeignKey(CafeBlock, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    review_text = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.author} – {self.rating}⭐"
    
class CafePhoto(models.Model):
    cafe = models.ForeignKey(CafeBlock,on_delete=models.CASCADE,related_name='photos')
    image = models.ImageField(upload_to='cafe_photos/')
    caption = models.CharField(max_length=255,blank=True)   


#TODO 4 Hide scrolebar

#TODO 6 Fix or add some overall html and css fixes to improve look of the site

