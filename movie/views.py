from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib
import base64

from .models import Movie
# Create your views here.

def home (request):
    #return HttpResponse('<H1>Welcome to homepage</h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name':'Daniela Arango'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
     #return HttpResponse("This is the About page")
     return render(request,'about.html')

def singup(request):
    email = request.GET.get('email')
    return render (request, 'singup.html', {'email':email})
 
def statistics_view(request): 
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()
    movie_counts_by_year = {}
    
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year [year] += 1
        else:
            movie_counts_by_year [year] = 1
            
    bar_width = 0.5
    
    bar_positions = range(len(movie_counts_by_year))
    
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png') 
    buffer.seek(0) 
    plt.close()
    
    image_png = buffer.getvalue() 
    buffer.close()  
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'statistics.html', {'graphic': graphic})



def genre_statistics_view(request): 
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()
    movie_counts_by_genre = {}
    
    for movie in all_movies:
        # Obtener el primer género de la película
        genres = movie.genre.split(',')
        first_genre = genres[0].strip() if genres else "None"
        
        if first_genre in movie_counts_by_genre:
            movie_counts_by_genre[first_genre] += 1
        else:
            movie_counts_by_genre[first_genre] = 1
            
    bar_width = 0.5
    
    bar_positions = range(len(movie_counts_by_genre))
    
    plt.bar(bar_positions, movie_counts_by_genre.values(), width=bar_width, align='center')
    
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_genre.keys(), rotation=90)
    
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png') 
    buffer.seek(0) 
    plt.close()
    
    image_png = buffer.getvalue() 
    buffer.close()  
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'genres.html', {'graphic': graphic})
