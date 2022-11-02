"""Account Model"""
#Import uuid module
import re
import uuid
from django_cryptography.fields import encrypt
from django.db import models
from django.urls import reverse # Cette fonction est utilisée pour formater les URL
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """UserManager manages the user data
    """
    PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

    def user_validator(self, data):
        """Validation of the User."""
        errors = {}
        user = User.objects.filter(username=data['username'])

        #will add alphanumeric validator later due to spaces
        if len(data['name'])<3:
            errors['name'] = 'Please Enter a Valid Name (Must Be At Least 3 Characters)'
        if len(data['username'])<3:
            errors['username'] = 'Please Enter a Valid Username (Must Be At Least 3 Characters)'
        if user:
            if user[0].username == data['username']:
                errors['username'] = "Username Used on Previous Registration. Please Login."
        #PASSWORD Validation of the User.
        if not self.PASSWORD_REGEX.match(data['password']):
            errors['password'] = 'Password must be Minimum eight characters, at least one '\
                'uppercase letter, one lowercase letter, one number, and one special character'
        if not data['confirm_password'] == data['password']:
            errors['confirm_password'] = "Passwords Must Match"
        return errors


    def login_validator(self, data):
        """login_validator"""
        errors_login = {}
        if len(data['username'])<3:
            errors_login['username'] = 'Please Enter a Valid Username (Must Be At Least 3 Characters)'
        if not self.PASSWORD_REGEX.match(data['password']):
            errors_login['password'] = 'Password must be Minimum eight characters, at least one '\
                'uppercase letter, one lowercase letter, one number, and one special character'
        return errors_login


    def create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        #email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a Super user with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)



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
class User(AbstractUser, models.Model):
    """Cet objet représente un utilisateur
        et éted l'objet User
    """
    password = encrypt(models.CharField(max_length = 50))
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
    objects = UserManager()

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
