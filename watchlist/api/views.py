from django.shortcuts import render
from watchlist.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist.api.serializers import MovieSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serlialier = MovieSerializer(movie)
    return Response(serlialier.data)