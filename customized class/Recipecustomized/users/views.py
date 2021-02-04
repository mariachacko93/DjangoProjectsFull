from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView,CreateView
from users.forms import UserCreationForm,registerForm,loginForm


# Create your views here.

class register(TemplateView):
    form_class=registerForm()
    template_name = "users/register_form.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=registerForm()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

class loginpage(TemplateView):
    form_class=loginForm()
    template_name = "users/login_form.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=loginForm
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data("username")
            password=form.cleaned_data("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
            return redirect("home")

def home(request):
    return render(request,"users/home.html")
















