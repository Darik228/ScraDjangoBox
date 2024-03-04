from django.db import models


class ScrapedData(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} -- {self.location}'