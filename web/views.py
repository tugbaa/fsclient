from django.shortcuts import render

# Create your views here.
from lib.clients import FsClient
from web.forms import SearchForm


def home(request):
	client = FsClient()
	response = None
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			near = form.cleaned_data['near']
			query = form.cleaned_data['query']
			response = client.search(near=near, query=query)
	else:
		form = SearchForm()

	return render(request, 'web/home.html', {'response': response, 'form': form})
