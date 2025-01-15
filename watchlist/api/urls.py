from django.urls import path
# from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import MovieListAV, MovieDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList, ReviewDetails
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream_details'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name="reviews-list"),
    path('stream/review/<int:pk>/', ReviewDetails.as_view(), name="review")

]


# for function based views
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie-details')
# ]
