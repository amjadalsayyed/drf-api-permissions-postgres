from django.urls import path
from .views import MoviesList, MovieDetail

urlpatterns = [
    path('', MoviesList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]