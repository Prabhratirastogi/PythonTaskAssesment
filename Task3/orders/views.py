from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    top_customers = Order.top_customers_last_6_months()
    return render(request, 'top_customers.html', {'customers': top_customers})
