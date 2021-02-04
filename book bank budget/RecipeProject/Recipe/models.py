from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=120)
    ingredients=models.CharField(max_length=500)
    category=models.CharField(max_length=120)
    recipe_img=models.ImageField(upload_to="images")
    created_by=models.CharField(max_length=120)

    def __str__(self):
        return self.recipe_name