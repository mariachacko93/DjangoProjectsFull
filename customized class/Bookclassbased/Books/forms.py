from Books.models import Books
from django.forms import ModelForm


class BookCreateForm(ModelForm):
    class Meta:
        model=Books
        fields="__all__"
