"""Account Model"""
#Import uuid module
import uuid
from django.db import models
from django.urls import reverse # Cette fonction est utilisée pour formater les URL
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

####################################################################################################
###  User
###  vue d’ensemble rapide de certains champs du modèle User :
###   - username  (nom d’utilisateur) — utilisé pour se connecter
###   - first_name  (prénom)
###   - last_name  (nom de famille)
###   - email
###   - password  (mot de passe) — les mots de passe sont stockés après hachage dans la base
###   de données. Ne sauvegardez jamais de mots de passe en clair.
###   - is_staff  (est un membre du personnel) — un booléen ; détermine si un utilisateur peut se
###   connecter au site administrateur Django.
###   - is_active  (est actif) — un booléen ; on considère que c’est une meilleure pratique
###   avec Django de signaler que des utilisateurs sont inactifs en réglant cet attribut sur  False
###   plutôt que de les supprimer.
###   - is_superuser  (est un superutilisateur) — un booléen ; les superusers, ou superutilisateurs,
###   obtiennent automatiquement toutes les permissions, telles que l’accès au site administrateur.
####################################################################################################
class User(AbstractUser):
    """Cet objet représente un utilisateur
        et éted l'objet User
    """
    code = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Unique ID for this user')
    photo = models.ImageField(upload_to='users/', blank=True)
    bio = models.TextField(max_length=160, help_text='About the User')
    country = models.CharField(max_length=50, blank=True)
    phone = PhoneNumberField(blank=True)
    url = models.URLField(max_length = 200)
    validated = models.BooleanField(default=False)
    validationcode = models.UUIDField(primary_key=False, default=uuid.uuid4,
        help_text='Validation ID for this user')
    invitedat = models.TimeField(null=True)
    createdat = models.TimeField(auto_now=False, auto_now_add=True)
    updatedat = models.TimeField(auto_now=True, auto_now_add=False)
    enabled = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        return str(self.code)

    def get_absolute_url(self):
        """Cette fonction est requise pas Django, lorsque
            vous souhaitez détailler le contenu d'un objet."""
        return reverse('user-detail', args=[str(self.code)])
