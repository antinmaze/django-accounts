"""Admin definition for Account"""
from account.models import User
from django.contrib import admin

# Register the admin class with the associated model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Cet objet représente l'objet admin Category """
    list_display = ('username','first_name','last_name','email',
       'is_staff','is_active','is_superuser',
        'code','photo','bio','country','phone','url','validated',
        'validationcode','invitedat','createdat','updatedat',
        'enabled')
    #hiding password from admin console
    exclude = ('password',)
