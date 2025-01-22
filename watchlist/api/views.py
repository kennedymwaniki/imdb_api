from django.shortcuts import get_object_or_404, render
from watchlist.models import WatchList, Student, StreamPlatform, Review
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from watchlist.api.serializers import WatchListSerializer, StudentSerializer, StreamPlatformSerializer, ReviewsSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from watchlist.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
# Create your views here.


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(pk=pk)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        user = self.request.user

        # Check if review exists
        review_queryset = Review.objects.filter(watchlist=watchlist, user=user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        # check if no of rating is 0
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (
                watchlist.avg_rating + serializer.validated_data['rating']) / 2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, user=user)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(pk=pk)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)

        user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=movie, user=user)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')

        serializer.save(watchlist=movie, user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "watchlist": WatchList.objects.get(pk=self.kwargs['pk']),
            "user": self.request.user
        })
        return context


# working with generic views with mixins
# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# working with class based views'
# APIVIEW


class MovieListAV(APIView):
    def get(request, self):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# streamPlatform views


class StreamPlatformAV(APIView):
    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()


# student views
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


# working with viewsets and routers
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # working with class based views

    # @api_view(['GET', 'POST'])
    # def movie_list(request):
    #     if request.method == 'GET':
    #         movies = WatchList.objects.all()
    #         serializer = WatchListSerializer(movies, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'POST':
    #         serializer = WatchListSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def movie_details(request, pk):
    #     try:
    #         movie = WatchList.objects.get(pk=pk)
    #     except WatchList.DoesNotExist:
    #         return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = WatchListSerializer(movie)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == 'PUT':
    #         serializer = WatchListSerializer(movie, data=request.data)
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
