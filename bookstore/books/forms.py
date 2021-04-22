from django.forms import ModelForm
from books.models import Books, Category, Isbn
from django.core.exceptions import ValidationError

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 10 or len(title) > 50 : 
            raise ValidationError("title must be between 10 and 50 chars")
        return title


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        print(name)
        if len(name) < 2 : 
            raise ValidationError("category name must have more than 2 charactrs")
        return name


class IsbnForm(ModelForm):
    class Meta:
        model = Isbn
        fields = "__all__"
        exclude = ("Isbn",)
