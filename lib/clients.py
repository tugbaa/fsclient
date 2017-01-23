from django.conf import settings
import logging
import requests


logger = logging.getLogger(__name__)


class FsClient(object):
	BASE_URL = "https://api.foursquare.com/v2"

	def search(self, near=None, query=None, *args, **kwargs):
		url = '%(base_url)s/venues/search?client_id=%(client_id)s' \
					'&client_secret=%(client_secret)s' \
					'&v=%(api_v_param)s' \
					'&near=%(near)s' \
					'&query=%(query)s' % {
						'base_url': FsClient.BASE_URL, 
						'client_id': settings.CLIENT_ID, 
						'client_secret': settings.CLIENT_SECRET, 
						'api_v_param': settings.API_V_PARAM,
						'near': near,
						'query': query}
		
		try:
			response = requests.get(url,  verify=False)
			return response.json()
		except Exception as e:
			logger.error(e)
			return None