from django.db import models


class SearchHistory(models.Model):
	near = models.CharField(max_length=50, null=True, blank=True)
	query = models.CharField(max_length=50, null=True, blank=True)		