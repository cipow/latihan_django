from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','picture','dokumen')

admin.site.register(Author, AuthorAdmin)

# Register your models here.
