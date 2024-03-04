from asgiref.sync import sync_to_async
from myscrapy.items import MyscrapyItem

class MyscrapyPipeline:
    @sync_to_async
    def process_item(self, item, spider):
        """
        Asynchronous method for processing and saving a Scrapy Item to a Django model.

        Args:
            item (MyscrapyItem): The Scrapy Item to be processed and saved.
            spider (scrapy.Spider): The Scrapy spider that generated this Item.

        Returns:
            MyscrapyItem: The processed Scrapy Item.
        """
        if isinstance(item, MyscrapyItem):
            # Saving the Item to the Django model asynchronously
            item.save()
        return item