from django.db import models

# Create your models here.

class sign_up(models.Model):
    Name = models.CharField(max_length=20)
    Mobile = models.IntegerField(max_length=10)
    Email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    password_check = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # add any additional fields you want to save



'''
class availability(models.Model):
    movie_availability: bool
    show_availability: bool
    screen_availability: bool
    ticket_availability: bool
'''

