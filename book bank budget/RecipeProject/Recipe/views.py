from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView,ListView,TemplateView
# Create your views here.
from Recipe.forms import RecipeCreateForm

class recipe_create(TemplateView):
    form_class = RecipeCreateForm()
    template_name ="recipes/recipe_form.html"
    context={}

    def get(self, request, *args):
        form=RecipeCreateForm()
        self.context["form"]=form
        return render(request,self.template_name,self.context)


