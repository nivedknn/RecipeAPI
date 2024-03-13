from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    Title=models.CharField(max_length=20)
    Cuisine=models.CharField(max_length=50)
    meals_type=models.CharField(max_length=20)
    Ingredients=models.TextField()
    Instruction=models.TextField()
    Created_at=models.DateTimeField()
    Upto_date=models.DateTimeField()

    def __str__(self):
        return self.Title

class Review(models.Model):
    recipe=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe