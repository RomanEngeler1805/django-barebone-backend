from django.urls import path

from .views import get_documents

urlpatterns = [
    path("documents/search", get_documents, name="search_documents"),
]
