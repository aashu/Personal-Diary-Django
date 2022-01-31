from django.urls import path
from . import views

urlpatterns = [
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='entry-detail'),
    path('', views.EntryListView.as_view(), name ='entry-list' )
]