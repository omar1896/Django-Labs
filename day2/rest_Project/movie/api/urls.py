from django.urls import path
from .views import (hello, movie_list, movie_create, movie_detail, movie_delete,
                     movie_update, MovieList, MovieDetail, MovieMixinList, MovieMixinsDetail,
                     MovieGenericsList, MovieGenericsDetail,
                     MovieViewSet)

from rest_framework.routers import DefaultRouter


app_name = "movie-api"

router = DefaultRouter()
router.register(r'movies_viewset', MovieViewSet, basename="movies")

urlpatterns = [
    # path('hello-api/', hello, name='hello'),
    path('hello-api/<str:mykey>', hello, name='hello'),
    path('api/movies', movie_list, name='movie-index'),
    path('api/movie/create', movie_create, name='movie-create'),
    path('api/movie/<int:pk>', movie_detail, name='movie-detail'),
    path('api/movie/<int:pk>/delete', movie_delete, name='movie-delete'),
    path('api/movie/<int:pk>/update', movie_update, name='movie-update'),
    # APi view
    path('movies_api_view/', MovieList.as_view()),
    path('movies_api_view/<int:pk>/', MovieDetail.as_view()),

    #mixins
    path('movies_mixins/', MovieMixinList.as_view()),
    path('movies_mixins/<int:pk>/', MovieMixinsDetail.as_view()),

    #generics
    path('movies_genrics/', MovieGenericsList.as_view()),
    path('movies_generics/<int:pk>/', MovieGenericsDetail.as_view()),

]

urlpatterns += router.urls