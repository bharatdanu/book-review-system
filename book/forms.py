from django import forms
from .models import Book

class BookFrm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title","author","description","genre","isbn",
                  "publication_date"]
        
        widgets = {
                    "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter title"}),
                    "author":forms.TextInput(attrs={"class":"form-control"}),
                    "description":forms.Textarea(attrs={"class":"form-control","rows":2}),
                    "genre":forms.Select(attrs={"class":"form-control"}),
                    "isbn":forms.TextInput(attrs={"class":"form-control"}),
                    "publication_date":forms.DateInput(attrs={"class":"form-control","placeholder":"yyyy-mm-dd"}),
                   }