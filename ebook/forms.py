from django import forms
from .models import Books
from django .core import validators
from django.contrib.auth.forms import UserCreationForm

CATEGORY = (
        ('Fantasy','Fantasy'),
        ('Literary','Literary'),
        ('Mystery','Mystery'),
        ('Non-Fiction','Non-Fiction'),
        ('Science','Science'),
        ('Fiction','Fiction'),
        ('Thriller','Thriller'),
    )
STAR = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class BookAddForm(forms.ModelForm):
    author = forms.CharField(max_length=200)
    category = forms.ChoiceField(choices=CATEGORY)
    title = forms.CharField(max_length=100)
    rating = forms.ChoiceField(choices=STAR)
    favourites = forms.BooleanField()
    image = forms.ImageField()

    class Meta:
        model = Books
        fields = ['author', 'category','title', 'rating','favourites','image']
    # to check exist or not
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data["title"]
        book = Books.objects.filter(title__iexact=title)
        if book:
            msg = "book already exist"
            self.add_error("title", msg)


class UpdateBookForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    review = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    rating = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    favourites = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))



class SearchForm(forms.Form):
    title=forms.CharField(max_length=50,widget=(forms.TextInput(attrs={'class':"form-control"})))
