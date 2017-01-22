from django import forms


class SearchForm(forms.Form):
	near = forms.CharField(label="near", max_length=50)
	query = forms.CharField(label="query", max_length=50)
