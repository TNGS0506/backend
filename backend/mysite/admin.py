from django.contrib import admin
from .models import Shoe, Category, Size, Feedback, ShoeImage

class SizeInline(admin.TabularInline):
    model = Size
    extra = 1

class ShoeImageInline(admin.TabularInline):
    model = ShoeImage
    extra = 1

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    inlines = [SizeInline, ShoeImageInline]
    list_display = ('name', 'price', 'category', 'created_date')
    search_fields = ('name', 'category__name')

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        
        # After saving related objects, check if an image was added to the shoe
        if 'image' in form.cleaned_data:
            shoe = form.instance
            image = form.cleaned_data['image']
            
            # Check if the image is already added to the images field
            if not shoe.images.filter(image=image).exists():
                # If not, add it to the images field
                ShoeImage.objects.create(shoe=shoe, image=image)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender', 'text', 'created_date')

admin.site.register(Category)
