from django import forms
from web.models import SearchHistory


class SearchForm(forms.ModelForm):
	class Meta:
		model = SearchHistory
		fields = "__all__"

			
