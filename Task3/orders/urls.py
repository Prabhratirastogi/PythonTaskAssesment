from django.urls import path
from .views import top_customers_view

urlpatterns = [
    path('top-customers/', top_customers_view, name='top_customers'),
]
