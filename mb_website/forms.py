from django import forms

class SearchBar(forms.Form):
    search = forms.CharField(max_length=200, label="Search Bar")