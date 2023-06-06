from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie.models import Movie
from .serializers import MovieSerializer
from django.core.exceptions import ObjectDoesNotExist

# Rewriting our API using class-based views
from django.http import Http404
from rest_framework.views import APIView
# using mixins
from rest_framework import mixins
from rest_framework import generics

#generics
from rest_framework import generics

#or
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

#viewsets
from rest_framework import viewsets
from rest_framework.decorators import action


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission


class UserCanDeleteMovie(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Can-Delete').exists():
            return True
        return False


# @api_view(['GET'])
# # @permission_classes([IsAdminUser])
# def hello(request):
#     data = {'message': f'Hello from rest api -> {request.user}'}
#     return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def hello(request, mykey):
    data = {'message': 'Hello from rest api your key is -> {}'.format(mykey)}
    if mykey == 'yes':
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    # print(request.user)
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance=movies, many=True)

    return Response(data=serialized_movies.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

    # Manipulate response
    data = {
        'message': 'Success',
        'data': {'id': serialized_movie.data.get('id')}
    }

    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail(request, pk):
    # try:
    #     movie_obj = Movie.objects.get(pk=pk)
    #     serialized_movie = MovieSerializer(instance=movie_obj)
    #     return Response(data=serialized_movie.data, status=status.HTTP_200_OK)
    # except ObjectDoesNotExist as error:
    #     return Response(data={'message':str(error)}, status=status.HTTP_400_BAD_REQUEST)
    response = {}
    movie_obj = Movie.objects.filter(pk=pk)
    print(movie_obj)
    if movie_obj.exists():
        movie_obj = movie_obj.first()
        serialized_movie = MovieSerializer(instance=movie_obj)

        response['data'] = serialized_movie.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'failed Movie does not exist'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['DELETE'])
@permission_classes([UserCanDeleteMovie])
def movie_delete(request, pk):
    response = {}
    try:
        movie_obj = Movie.objects.get(pk=pk)
        movie_obj.delete()
        response['data'] = {'message': 'Successfully Deleted Movie'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except Exception as e:
        response['data'] = {'message': 'Error While Deleting Movie -- {} -- Target Movie {}'.format(str(e), pk)}
        response['status'] = status.HTTP_400_BAD_REQUEST

    print("Result -> ", response)
    return Response(**response)


@api_view(['PUT', 'PATCH'])
# @permission_classes([IsAuthenticated])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serialized_movie = MovieSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie, data=request.data, partial=True)

    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(data=serialized_movie.data, status=status.HTTP_200_OK)

    return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

#Rewriting our API using class-based views

class MovieList(APIView):
    """
    List all movies, or create a new movie.
    """
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetail(APIView):
    """
    Retrieve, update or delete a movie instance.
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

# mixins 
class MovieMixinList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    

class MovieMixinsDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    
    #Using generic class-based views

class MovieGenericsList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer




# class MovieClassCreate(CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     lookup_field = 'pk'

# #
# class MovieClassDelete(DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     lookup_field = 'pk'
#
    # def delete(self, request, *args, **kwargs):
    #     if request.data.get('pk'):
    #         # delete single obj
    #         pass
    #     else:
    #         self.queryset.delete()


#viewsets
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        movie = self.get_object()
        return Response(movie.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    