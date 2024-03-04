from scrapy_djangoitem import DjangoItem
from myapp.models import ScrapedData

class MyscrapyItem(DjangoItem):
    """
    Scrapy Item class that represents the structure of data to be scraped and stored in the Django model.

    Attributes:
        django_model (Django model): The Django model to which the scraped data will be saved.

    """
    django_model = ScrapedData  # Specifying the Django model to be associated with this Scrapy Item
