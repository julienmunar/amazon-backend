from distutils.command.upload import upload
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

import os
import uuid
import random
from datetime import datetime

def user_directory_path(instance,filename):
    user=str(instance.username) 
    todays_date=datetime.today()
    path="myUser/img/{}/{}".format(todays_date.year,user)
    filename_reformat= user+"-" + str(todays_date.year)+"_"+str(todays_date.month)+"_"+str(todays_date.day)+"."+ filename

    return os.path.join(path, filename_reformat)

class MyUserManager (BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Please enter your email")
        if not username:
            raise ValueError("Please enter a username")
        user=self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password=None):
        user = self.create_user(email,username=username,password=password)

        user.is_active=True
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address', max_length=50,unique=True)
    username=models.CharField(max_length=30, null=True,unique=True)
    firstname=models.CharField(max_length=30,null=True)
    lastname=models.CharField(max_length=30, null=True)
    avatar=models.ImageField(null=True,blank=True,upload_to=user_directory_path)
    is_active=models.BooleanField(default=False,help_text=' Indique si cet utilisateur doit être considéré comme actif.')
    is_admin = models.BooleanField(default=False,help_text=' Indique si cet utilisateur peut accéder au site d’administration === is_staff.')
   
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return (f"{self.firstname}, {self.lastname} -- (Email Address: {self.email}) ")
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True    
    

    @property
    def is_staff(self):
        return self.is_admin

    