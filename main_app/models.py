from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.color}{self.name}"
    
    def get_absolute_url(self):
        return reverse('character_detail', kwargs={'pk': self.id})

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    current_rank = models.IntegerField(default=1)
    alltime_rank = models.IntegerField(default=1)
    
    characters = models.ManyToManyField(Character)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'player_id': self.id})
    
class Win(models.Model):
    tourney_wins = models.CharField(max_length=100)
    date = models.DateField()

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f'This player won {self.tourney_wins}'
    
    class Meta: 
        ordering = ['-date']
    
   

