"""Good Model"""
#Import uuid module
import uuid
from django.db import models
from django.urls import reverse # Cette fonction est utilisée pour formater les URL
from account.models import User as account_user

####################################################################################################
###  Category
####################################################################################################
class Category(models.Model):
    """Cet objet représente une catégorie d'objets.
        Category
        Name
        Code
        Description
    """
    name = models.CharField(max_length=200, help_text='Enter a category of good')
    code = models.UUIDField(primary_key=False,
        default=uuid.uuid4,help_text='Unique ID for this category of good')
    description = models.TextField(max_length=1000, help_text='description of the Category')   

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return str(self.code)
        #return self.name + self.code


    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque
        vous souhaitez détailler le contenu d'un objet."""
        return reverse('category-detail', args=[str(self.code)])

####################################################################################################
###  SubCategory
####################################################################################################
class SubCategory(models.Model):
    """Cet objet représente une subcatégorie d'objets.
        IdSubCategory
        Name
        Code
        Description
        #IdCategory
    """
    name = models.CharField(max_length=200, help_text='Enter a subcategory of good')
    code = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Unique ID for this subcategory of good')
    description = models.TextField(max_length=1000, help_text='description of the SubCategory')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return str(self.code)
        #return self.name

    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque
        vous souhaitez détailler le contenu d'un objet."""
        return reverse('subcategory-detail', args=[str(self.code)])

####################################################################################################
###  OwnerGroup
####################################################################################################
class OwnerGroup(models.Model):
    """Cet objet représente un groupe de propriétaire (OwnerGroup).
        IdOwnerGroup
        Name
        Code
        Url
        CreatedAt
        UpdatedAt
        Enabled
    """
    name = models.CharField(max_length=200, help_text='Enter a OwnerGroup of good')
    code = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Unique ID for this OwnerGroup of good')
    url = models.URLField(max_length = 200)
    createdat = models.TimeField(auto_now=False, auto_now_add=True)
    updatedat = models.TimeField(auto_now=True, auto_now_add=False)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return str(self.code)
        #return self.name


    def get_absolute_url(self):
        """Cette fonction est requise pas Django,
        lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('ownergroup-detail', args=[str(self.code)])

####################################################################################################
###  Owner
####################################################################################################
class Owner(models.Model):
    """Cet objet représente la constitution du groupe de propriétaire (Onwer).
        IdOwner
        #IdOwnerGroup
        #IdUser => DISABLED
        isAdmin
        Code
        CreatedAt
        UpdatedAt
        Enabled
    """
    isadmin = models.BooleanField()
    code = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Unique ID for this OwnerGroup of good')
    createdat = models.TimeField(auto_now=False, auto_now_add=True)
    updatedat = models.TimeField(auto_now=True, auto_now_add=False)
    enabled = models.BooleanField(default=True)

    ownergroup = models.ForeignKey('OwnerGroup',on_delete=models.CASCADE)
    user = models.ForeignKey(account_user,on_delete=models.CASCADE)


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return str(self.code)
        #return self.name


    def get_absolute_url(self):
        """Cette fonction est requise pas Django,
            lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('owner-detail', args=[str(self.code)])

####################################################################################################
###  Good
####################################################################################################
class Good(models.Model):
    """Cet objet représente un objet (Good)).
        IdGood
        Name
        Summary
        Description
        #IdCategory (Not NULL)
        #IdSubcategory (Not NULL)
        #IdOwnerGroup (Not NULL)
        Code
        Url
        Status
        Image1
        Image2
        Image3
        State
        CreatedAt
        UpdatedAt
        Enabled
    """
    name = models.CharField(max_length=200, help_text='Enter a Good item')
    summary = models.TextField(max_length=300, help_text='summary of the Good')
    description = models.TextField(max_length=1000, help_text='description of the Good')
    #IdCategory (Not NULL)
    #IdSubcategory (Not NULL)
    #IdOwnerGroup (Not NULL)
    code = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Unique ID for this OwnerGroup of good')
    url = models.URLField(max_length = 200)
    #STATUS MANAGEMENT
    STATUS_AVAILABLE = 'AV'
    STATUS_OUT = 'OT'
    STATUS_BOOKED = 'BK'
    STATUS_CANCELED =  'CA'
    STATUS_CONFIRMED =  'CN'
    STATUS_COMPLETED =  'CM'
    STATUS = (
        (STATUS_AVAILABLE, 'Available'),
        (STATUS_OUT, 'Out'),
        (STATUS_BOOKED, 'Booked'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_COMPLETED, 'Completed'),
    )
    status = models.CharField(max_length=2, choices=STATUS,
        default=STATUS_AVAILABLE, help_text='Status a Good item')
    # file could be uploaded to MEDIA_ROOT / uploads
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    #STATE MANAGEMENT
    STATE_NEW = 'N'
    STATE_VGS = 'V'
    STATE_GS = 'G'
    STATE_SAT = 'S'
    STATE = (
        (STATE_NEW, 'New Condition'),
        (STATE_VGS, 'Very Good State'),
        (STATE_GS, 'Good State'),
        (STATE_SAT, 'Satisfactory State'),
    )
    state = models.CharField(max_length=1, choices=STATE,
        default=STATE_NEW, help_text='State of a Good item')
    createdat = models.TimeField(auto_now=False, auto_now_add=True)
    updatedat = models.TimeField(auto_now=True, auto_now_add=False)
    enabled = models.BooleanField(default=True)

    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory',on_delete=models.CASCADE)
    ownergroup = models.ForeignKey('OwnerGroup',on_delete=models.CASCADE)


    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier 
           l'instance de la classe d'objet."""
        return str(self.code)
        #return self.name


    def get_absolute_url(self):
        """Cette fonction est requise pas Django,
        lorsque vous souhaitez détailler le contenu d'un objet."""
        return reverse('good-detail', args=[str(self.code)])

####################################################################################################
###  END
####################################################################################################
