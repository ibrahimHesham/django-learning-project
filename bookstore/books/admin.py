from django.contrib import admin
from .models import Books, Category, Isbn
from .forms import BooksForm, CategoryForm, IsbnForm
# from django import forms
# from django.core.exceptions import ValidationError

class BookInline(admin.TabularInline):
    model = Books
    form = BooksForm

class BookAdmin(admin.ModelAdmin):
    form = BooksForm
    list_display = ("title","author")
    list_filter  = ("categories",)
    search_fields = ("title", )

class IsbnAdmin(admin.ModelAdmin):
    form = IsbnForm
    inlines = [
        BookInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm



# Register your models here.
admin.site.register(Books, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Isbn, IsbnAdmin)

