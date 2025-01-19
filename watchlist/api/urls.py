from django.urls import path
from rest_framework.routers import DefaultRouter
# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import MovieListAV, MovieDetailsAV, ReviewCreate, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList, ReviewDetails
router = DefaultRouter()

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream_details'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name="reviews-list"),
    # path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name="reviews-create"),
    path('stream/review/<int:pk>/', ReviewDetails.as_view(), name="review")

]


# for function based views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie-details')
# ]
