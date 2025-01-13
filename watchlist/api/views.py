from django.shortcuts import render
from watchlist.models import Movie, Student
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from watchlist.api.serializers import MovieSerializer, StudentSerializer
# Create your views here.


# working with class based views'
# APIVIEW
class MovieListAV(APIView):
    def get(request, self):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # working with class based views

    # @api_view(['GET', 'POST'])
    # def movie_list(request):
    #     if request.method == 'GET':
    #         movies = Movie.objects.all()
    #         serializer = MovieSerializer(movies, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'POST':
    #         serializer = MovieSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def movie_details(request, pk):
    #     try:
    #         movie = Movie.objects.get(pk=pk)
    #     except Movie.DoesNotExist:
    #         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = MovieSerializer(movie)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'PUT':
    #         serializer = MovieSerializer(movie, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if request.method == "DELETE":
    #         movie.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    # # ! this is for practice only
    # @api_view(['GET', 'POST'])
    # def students(request):
    #     if request.method == 'GET':
    #         students = Student.objects.all()
    #         serializer = StudentSerializer(students, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'POST':
    #         serializer = StudentSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    # def student_details(request, pk):
    #     try:
    #         student = Student.objects.get(pk=pk)
    #     except Student.DoesNotExist:
    #         return Response({'error': 'student not found'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = StudentSerializer(student)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'PUT':
    #         serializer = StudentSerializer(student, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     if request.method == 'DELETE':
    #         student.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)


class StudentsAv(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailsAv(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'student not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
