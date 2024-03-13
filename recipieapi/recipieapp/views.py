from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import viewsets,mixins
from .models import Recipe,Review
from .serializers import UserSerializer,RecipeSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated



class CreateUser(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserSerializer

class RecipeView(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Title', 'Cuisine', 'meals_type']

class ReviewView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):
    permission_classes = [IsAuthenticated,]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer






