from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from budget.forms import LoginForm
from budget.forms import RegistrationForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form

    return render(request,"budget/register.html",context)

def signIn(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            print("inside")
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            print(password,",",username)
            if user:

                login(request,user)
                return render(request,"budget/home.html")
            else:
                context["form"]=form
                return render(request,"budget/login.html",context)
        else:
            context["form"] = form
            return render(request, "budget/login.html", context)

    return render(request,"budget/login.html",context)

def SignOut(request):
    logout(request)
    return redirect("login")


def editProfile(request):
    user =User.objects.get(username=request.user)
    form=RegistrationForm(instance=user)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("SignIn")
    else:
        context["form"]=form
        return render(request, "budget/edit.html", context)

    return render(request,"budget/edit.html",context)

def homePage(request):
    return render(request,"budget/home.html")


from budget.forms import AddExpensesForm
from budget.models import Expenses
def addExpens(request):
    form=AddExpensesForm()
    context={}
    context["form"]=form
    expenses=Expenses.objects.filter(user=request.user)
    context["expenses"]=expenses
    if request.method=="POST":
        form=AddExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expens")

    return render(request,"budget/addexpens.html",context)

