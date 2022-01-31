from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')

class EntryDetailView(DetailView):
    model = Entry

