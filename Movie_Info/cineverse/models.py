from django.db import models

# Create your models here.

class Movie(models.Model):
    Name: str          # Name of the movie
    lang: str          # Language of the movie
    screen: str        # screens at which movie is Playing
    Details: str       # show running length
    prices: str        # price - price format (For future requirement)
    shows: str         # At what shows movie is playing
    icon: str          # Poster of the movie
    link: str          # Trailer Links (YouTube)
    availability: str  # comment on sets filling / availability
    available: str     # Based on availability of shows for a movie
    upcoming: bool     # Differentiates between existing and upcoming movies
    upd: bool          # Available (or) Houseful

    class Meta:
        app_label = 'cineverse'

    def __str__(self):
        return self.Name

class screen(models.Model):
    show_movie: str   # Movie Name
    show_s1: str      # Shows playing of movie in a screen1
    show_s2: str      # Shows playing of movie in a screen2
    show_s3: str      # Shows playing of movie in a screen3


    class Meta:
        app_label = 'cineverse'

    def __str__(self):
        return self.show_movie
class review(models.Model):
    Name: str    # Movie Name
    rating: str  # IMDb rating of the Movie

    class Meta:
        app_label = 'cineverse'

    def __str__(self):
        return self.Name
class timings(models.Model):
    Name: str   # No use
    cost1: str  # Cost of platinum class seats
    cost2: str  # Cost of golden class seats
    cost3: str  # Cost of silver class seats
    sc1: str    # To display timings , unorthodox way
    sc2: str    # To display timings , unorthodox way
    sc3: str    # To display timings , unorthodox way

    class Meta:
        app_label = 'cineverse'

    def __str__(self):
        return self.Name



