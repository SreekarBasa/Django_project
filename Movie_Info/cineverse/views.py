from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from cineverse.models import Movie, screen, review, timings
 # Also can be done using CSV files....
def home(request):
    movie1 = Movie()
    movie2 = Movie()
    movie3 = Movie()
    movie4 = Movie()
    movie5 = Movie()

    movie1.Name = 'Sita Ramam'
    movie1.lang = 'Telugu'
    movie1.Details = '124 minutes'
    movie1.prices = ' 90/- , 150/- , 250/- '
    movie1.link = 'https://www.youtube.com/watch?v=Ljk6tGZ1l3A'
    movie1.icon = 'sita_ramam.jpg'
    movie1.availability = 'Not Available'
    movie1.upcoming = False
    movie1.upd = True

    movie2.Name = 'Vikram'
    movie2.lang = 'Telugu'
    movie2.Details = '177 minutes'
    movie2.prices = ' 90/- , 150/- , 250/- '
    movie2.link = 'https://www.youtube.com/watch?v=WC5X3i0B4cg'
    movie2.icon = 'vikram.jpg'
    movie2.availability = 'Filling Fast'
    movie1.upcoming = False
    movie2.upd = False

    movie3.Name = 'Thor Love and Thunder-3D'
    movie3.lang = 'English'
    movie3.Details = '119 minutes'
    movie3.prices = ' 80/- , 140/- , 220/- '
    movie3.link = 'https://www.youtube.com/watch?v=Go8nTmfrQd8'
    movie3.icon = 'thor4.jpg'
    movie3.availability = 'Available'
    movie1.upcoming = False
    movie3.upd = False

    movie4.Name = 'Black Panther: Wakanda Forever'
    movie4.lang = 'English, Telugu'
    movie4.Details = '11th November,2022'
    movie4.prices = ' 90/- , 150/- , 250/- '
    movie4.link = 'https://www.youtube.com/watch?v=RlOB3UALvrQ'
    movie4.icon = 'black2.jpg'
    movie4.availability = 'Not yet opened'
    movie4.upcoming = True
    movie4.upd = False

    movie5.Name = 'LIGER'
    movie5.lang = 'Telugu'
    movie5.Details = '25th August,2022'
    movie5.prices = ' 90/- , 150/- , 250/- '
    movie5.link = 'https://www.youtube.com/watch?v=koYN8qSk_Us'
    movie5.icon = 'liger.jpg'
    movie5.availability = 'Not yet opened'
    movie5.upcoming = True
    movie5.upd = False

    shows = [movie1, movie2, movie3, movie4, movie5]

    return render(request, "index.html", {'shows': shows})

def info(request):
    movie1 = Movie()
    movie1.Name = 'Sita Ramam'
    movie1.screen = 'Screen - 2,3'
    movie1.Shows = ' All Shows'
    movie1.available = ' NIL '
    movie1.link = 'https://en.wikipedia.org/wiki/Sita_Ramam'

    movie2 = Movie()
    movie2.Name = 'Vikram'
    movie2.screen = 'Screen - 1'
    movie2.Shows = ' All Shows'
    movie2.available = ' Filling Fast ; Available : 1,2,5 '
    movie2.link = 'https://en.wikipedia.org/wiki/Vikram_(2022_film)'

    movie3 = Movie()
    movie3.Name = 'Thor Love and Thunder'
    movie3.screen = 'Screen - 3'
    movie3.Shows = 'Shows - 1,2,3 '
    movie3.available = ' 1,2,3 '
    movie3.link = 'https://en.wikipedia.org/wiki/Thor:_Love_and_Thunder'

    shw1 = screen()
    shw1.show_movie = 'Sita Ramam'
    shw1.show_s1 = ' - '
    shw1.show_s2 = ' shows - 1,2,3,4,5 '
    shw1.show_s3 = ' shows - 4,5'

    shw2 = screen()
    shw2.show_movie = 'vikram'
    shw2.show_s1 = 'shows - 1,2,3,4,5 '
    shw2.show_s2 = ' - '
    shw2.show_s3 = ' - '

    shw3 = screen()
    shw3.show_movie = 'Thor Love and Thunder'
    shw3.show_s1 = ' - '
    shw3.show_s2 = ' - '
    shw3.show_s3 = ' shows - 1,2,3'

    show = [movie1, movie2, movie3]
    scrn = [shw1, shw2, shw3]

    return render(request, 'Info.html', {'scrn': scrn, 'show': show})

def reviews(request):
    review1 = review()
    review1.Name = 'Vikram'
    review1.rating = '8.5/10 IMDb'

    review2 = review()
    review2.Name = 'Sita Ramam'
    review2.rating = '9.0/10 IMDb'

    review3 = review()
    review3.Name = 'Thor Love and Thunder'
    review3.rating = '6.7/10 IMDb'

    Review = [review1, review2, review3]

    return render(request, 'reviews.html', {'Review': Review})

def mov1(request):
    film = Movie()
    film.Name = 'Vikram'
    film.icon = 'vikram1.jpg'
    film.link = 'https://www.youtube.com/watch?v=WC5X3i0B4cg'
    return render(request, 'mov1.html', {'film': film})
def mov2(request):
    film = Movie()
    film.link = 'https://www.youtube.com/watch?v=Ljk6tGZ1l3A'
    return render(request, 'mov2.html', {'film': film})
def mov3(request):
    film = Movie()
    film.link = 'https://www.youtube.com/watch?v=Go8nTmfrQd8'
    return render(request, 'mov3.html', {'film': film})

def timing(request):
    ptr = timings()
    ptr.cost1 = 'Platinum : 250/- ; Gold : 150/- ; Silver : 90/-'
    ptr.cost2 = 'Platinum : 250/- ; Gold : 150/- ; Silver : 90/-'
    ptr.cost3 = 'Platinum : 220/- ; Gold : 140/- ; Silver : 80/-'
    ptr.sc1 = '00'
    ptr.sc2 = '20'
    ptr.sc3 = '35'
    pt = [ptr]
    return render(request, 'Timings.html', {'pt': pt})
def signup(request):
    return render(request, 'signup.html')
def About_us(request):
    return render(request, 'Aboutus.html')







