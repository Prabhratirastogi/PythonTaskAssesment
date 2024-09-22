from django.db import models
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

    @classmethod
    def top_customers_last_6_months(cls):
        six_months_ago = now() - timedelta(days=6*30)
        top_customers = (
            cls.objects.filter(order_date__gte=six_months_ago)
            .values('customer__name')  # Get the customer's name
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )

        # Fetching additional details for each customer's top order
        for customer in top_customers:
            customer_orders = cls.objects.filter(customer__name=customer['customer__name'], order_date__gte=six_months_ago).order_by('-order_date')
            if customer_orders.exists():
                customer['status'] = customer_orders.first().status
                customer['order_date'] = customer_orders.first().order_date

        return top_customers
