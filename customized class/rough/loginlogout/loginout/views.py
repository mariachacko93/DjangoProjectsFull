from django.shortcuts import render,redirect
from loginout.forms import LoginForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from loginout.models import LoginModel

class LoginView(TemplateView):
    model=LoginModel
    template_name = "loginout/login.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form=LoginForm()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        # else:
        #     self.context["form"] = form
        #     return render(request, self.template_name, self.context)

class logoutView(TemplateView):
    template_name = "loginout/home.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class Homepage(TemplateView):
    template_name = "loginout/home.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)