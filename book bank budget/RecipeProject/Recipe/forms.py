from django.forms import ModelForm
from Recipe.models import Recipe

class RecipeCreateForm(ModelForm):
    class Meta:
        model=Recipe
        fields="__all__"