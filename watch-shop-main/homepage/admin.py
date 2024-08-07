from django.contrib import admin

from . models import Watches,CartItem
from . models import WatchesUploads
from . models import Wishlisst,Cart,WatchReview
# Register your models here.

admin.site.register(Watches)

### Watch uploads 
class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('name','price','description','image')
    list_filter = ('name','price')
    search_fields = ('name','description')
    fields = ['name','price','description','image','count']

admin.site.register(WatchesUploads,WatchesUploadsAdmin)

## Wishlist
class WishlisstAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
admin.site.register(Wishlisst,WishlisstAdmin)
#admin.site.register(Wishlisst)

# cart 
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user','product')
#     list_filter = ('user','product')
admin.site.register(Cart)
admin.site.register(CartItem)

## Watch Riview
class WatchReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','rating','review_text')
    list_filter = ('user','product','rating')
admin.site.register(WatchReview,WatchReviewAdmin)




