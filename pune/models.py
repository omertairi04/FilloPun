from django.db import models
import uuid
from django.contrib.auth.models import User

from users.models import Profile , Skills

EXPERIENCE = (
    ('Fillestar', 'Fillestar'),
    ('1-2 vjet pervoje' , '1-2 vjet pervoje'),
    ('3-6 vjet pervoje' , '3-6 vjet pervoje'),
    ('7+ vjet pervoje' , '7+ vjet pervoje')
)

class Pune(models.Model):
    business = models.ForeignKey(Profile , on_delete=models.CASCADE , blank=True)
    title = models.CharField(max_length=255)
    bio = models.TextField(blank=True , null=True)
    image = models.ImageField(blank=True , null=True, upload_to='profiles/', default='static/images/default.jpg')
    location = models.CharField(max_length=200 , blank=True , null=True)
    perkohshmeri = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skills, blank=True)
    experience = models.CharField(max_length=255 , choices=EXPERIENCE)
    pagesa = models.DecimalField(decimal_places=2 , max_digits=10)
    orari = models.PositiveIntegerField(default=0)
    aplicants = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , 
                        primary_key=True , editable=False)

    def __str__(self):
        return str(self.title)

class Apliko(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_likes')
    post = models.ForeignKey(Pune , on_delete=models.CASCADE , related_name='post_likes')


    def __str__(self):
        return str(f'{self.user} - {self.post}')