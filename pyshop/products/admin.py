from django.contrib import admin
from . models import Product
from . models import Offer


# ====================================================================
# 1:- Customizing our Product table in the admin area: (ProductAdmin)
# 2:- Customizing ourt Offer table in the admin area: (OfferAdmin)
# ====================================================================
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Register your models here.
# ======================================
# To register/add model to our database
# ======================================
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
