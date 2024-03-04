import scrapy
from myscrapy.items import MyscrapyItem


class SpiderMan(scrapy.Spider):
    """
    Spider class to crawl and scrape data from the given start URL.

    Attributes:
        name (str): The name of the spider.
        start_urls (list): The list of start URLs for the spider.
        count (int): Counter for the number of items processed.
        max_items (int): Maximum number of items to scrape.

    Methods:
        parse(self, response): The main parsing method for extracting data.

    """
    name = "spiderman"
    start_urls = ["https://www.bezrealitky.cz/vyhledat?offerType=PRODEJ&estateType=BYT&currency=CZK"]
    count = 0
    max_items = 500

    def parse(self, response):
        """
        Parse method to extract data from the given response.

        Args:
            response (scrapy.http.Response): The response object containing the HTML content.

        Yields:
            MyscrapyItem: The scraped item with title, image_url, and location.

        """
        for property_card in response.css("article.PropertyCard_propertyCard__moO_5"):
            if self.count >= self.max_items:
                break

            yield MyscrapyItem(
                title=property_card.css("h2 a span.PropertyCard_propertyCardLabel__HN3Jo span::text").get(),
                image_url=response.urljoin(property_card.css("figure img::attr(src)").get()),
                location=property_card.css("h2 a span.PropertyCard_propertyCardAddress__hNqyR::text").get()
            )

            self.count += 1

            yield from response.follow_all(
                css="ul.pagination li.page-item.active + li.page-item a.page-link::attr(href)",
                callback=self.parse
            )
