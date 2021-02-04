from django.shortcuts import render,redirect

# Create your views here.
# listview
# detailView
# createView
# deleteview
# upadteview
from django.views.generic import TemplateView
from Books.forms import BookCreateForm
from Books.models import Books
from django.urls import reverse_lazy

class bookcreate(TemplateView):
    form_class=BookCreateForm()
    template_name = "books/book_form.html"
    context={}


    def get(self, request, *args, **kwargs):
        form=BookCreateForm()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("booklist")


class booklist(TemplateView):
    model=Books
    template_name = "books/book_list.html"

    context={}
    def get_query_set(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context["books"]=self.get_query_set()
        return render(request,self.template_name,self.context)


class bookedit(TemplateView):
    model=Books
    template_name ="books/book_edit.html"
    context={}
    def get_query_set(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        book=self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request, *args, **kwargs):
        book = self.get_query_set(kwargs.get("pk"))
        form=BookCreateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("booklist")


class bookdelete(TemplateView):
    model=Books
    def get_query_set(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        book=self.get_query_set(kwargs.get("pk"))
        book.delete()
        return redirect("booklist")
