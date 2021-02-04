from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.
from users.forms import UserCreationForm,RegistrationForm,LoginForm
from django.views.generic import TemplateView,CreateView


class register(CreateView):
    form_class = RegistrationForm()
    template_name ="users/user_form.html"
    context={}

    def get(self, request, *args, **kwargs):
        form =self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class loginView(TemplateView):
    form_class=LoginForm()
    template_name = "users/userlogin.html"
    context={}

    def get(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        self.context["form"]=form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        self.context["form"]=form
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            return render(request,self.template_name,self.context)


class home(CreateView):
    template_name = "users/home.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

