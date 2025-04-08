from django.contrib import admin
from .models import CafeBlock,Review,CafePhoto

    
class CafePhotoInline(admin.TabularInline):
    model = CafePhoto
    extra = 1
    fields = ('image', 'caption')

@admin.register(CafeBlock)
class CafeBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'site_url', 'photo','full_description','google_map_embed')
    inlines = [CafePhotoInline]
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'cafe', 'rating', 'date')
    list_filter = ('cafe', 'rating')
    search_fields = ('author', 'review_text')
