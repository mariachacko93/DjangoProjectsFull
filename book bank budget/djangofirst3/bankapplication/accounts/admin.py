from django.contrib import admin

# Register your models here.
from accounts.models import CreateAccount

admin.site.register(CreateAccount)
