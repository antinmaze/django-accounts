"""Admin definition for Good"""
from django.contrib import admin
from good.models import Category, SubCategory, OwnerGroup, Owner, Good

# Register the admin class with the associated model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin Category """
    list_display = ('name', 'code', 'description')

# Register the admin class with the associated model
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin SubCategory """
    list_display = ('name', 'code', 'description', 'category') 
    #list_filter = ('category')

# Register the admin class with the associated model
@admin.register(OwnerGroup)
class OwnerGroupAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin OwnerGroup """
    list_display = ('name', 'code', 'url', 'createdat', 'updatedat', 'enabled') 

# Register the admin class with the associated model
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin Owner """
    list_display = ('code', 'isadmin', 'createdat', 'updatedat', 'enabled', 'ownergroup')
     
# Register the admin class with the associated model
@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin Good """
    list_display = ('name',  'code',  'url', 'status', 'state', 'summary', 'description', 
        'createdat', 'updatedat', 'enabled', 'category', 'subcategory', 'ownergroup')
    list_filter = ('status', 'state', 'category', 'subcategory')
