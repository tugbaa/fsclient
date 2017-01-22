import logging

from django.shortcuts import render

from lib.clients import FsClient
from web.forms import SearchForm
from web.models import SearchHistory


logger = logging.getLogger(__name__)


def home(request):
	client = FsClient()
	response = None
	if request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			response = client.search(**form.cleaned_data)
			try:
				form.save()
			except Exception as e:
				logger.error(e)
	else:
		form = SearchForm()

	history = SearchHistory.objects.all()
	return render(request, 'web/home.html', {
		'response': response, 
		'form': form, 
		'history': history})
