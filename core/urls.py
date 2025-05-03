from django.urls import path
from .views import MarcaList

urlpatterns = [
    path('marcas/', MarcaList.as_view(), name='marca-list'),
]