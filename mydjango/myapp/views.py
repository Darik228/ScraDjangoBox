from django.views.generic import ListView
from .models import ScrapedData


class ScrapedDataView(ListView):
    model = ScrapedData
    template_name = 'index.html'
    context_object_name = 'scraped_data_list'
    paginate_by = 100