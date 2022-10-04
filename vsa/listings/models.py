from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Band(models.Model):
    
    def __str__(self) -> str:
        return f'{self.name}'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2023)]
        )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True,blank=True)
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    
class Title(models.Model):
    title = models.fields.CharField(max_length=100)

class Listing(models.Model):
    band = models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
    name = models.fields.CharField(max_length=100)
    
    

