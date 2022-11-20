from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE ,  null=True , blank=True)
    name = models.CharField(max_length=150 , null=True , blank=True)
    sur_name = models.CharField(max_length=150 , null=True , blank=True)
    email = models.EmailField(max_length=500 , blank=True , null=True)
    username = models.CharField(max_length=200 ,unique = True ,blank=True , null=True) 
    profilepic = models.ImageField(blank=True , null=True, upload_to='profiles/', default='images/profiles/user-default.png')
    bio = models.TextField(blank=True , null=True)
    skills = models.ManyToManyField('Skills', blank=True)
    # Upload CV
    # Resume
    birth_date = models.DateField(blank=True, null=True)
    # per business / fusha~field
    location = models.CharField(max_length=200 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , 
                        primary_key=True , editable=False)

    def __str__(self):
        return str(self.username)

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

class Skills(models.Model):
    name = models.CharField(max_length=200 , blank=True , null=True)
    description = models.TextField(blank=True , null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , 
                        primary_key=True , editable=False)

    def __str__(self):
        return str(self.name)
