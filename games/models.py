from django.db import models

# Create your models here.

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name    = models.CharField(max_length=200, unique=True)
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played   = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    MALE='M'
    FEMALE='F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    created = models.DateTimeField(auto_now_add=True)
    name    = models.CharField(max_length=50, blank=False, default='', unique=True)

    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )

    class Meta:
        ordering = ('name'),


    def __str__(self):
        return self.name


    

