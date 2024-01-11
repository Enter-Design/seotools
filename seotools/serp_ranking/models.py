from django.db import models

# Create your models here.


class SerpResult(models):
    search_query = models.CharField(max_length=200)
    date = models.DateTimeField("query date")
    result = models.JSONField()

    def __str__(self):
        return self.search_query
