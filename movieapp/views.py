from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies


# Create your views here.
def index(request):

    movies = Movies.objects.all()[:10]
    movie_list = []

    for m in movies:

        movies_list = {
            'name' : m.name,
            'location' : m.location,
            'timimg' : m.timimg,

        }



        movie_list.append(movies_list)

    context = {
        'movies': movies
    }

    return render(request,'index.html',context)



def details(request,id):
    movies_l = Movies.objects.get(id=id)

    context = {
        'movies': movies
        }

    return render(request,'details.html',context)
