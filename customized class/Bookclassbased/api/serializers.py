
from rest_framework.serializers import ModelSerializer
from Books.models import Books

class bookSerializers(ModelSerializer):
    class Meta:
        model=Books
        fields=["book_name","pages","price","author"]