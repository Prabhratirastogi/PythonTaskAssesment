from django.test import TestCase
from django.utils import timezone
from .models import Customer, Order

class OrderModelTest(TestCase):

    def setUp(self):
        # Create some customers
        self.customer1 = Customer.objects.create(name="Alice")
        self.customer2 = Customer.objects.create(name="Bob")

        # Create some orders
        now = timezone.now()
        Order.objects.create(customer=self.customer1, order_date=now, status="completed", total_amount=100.00)
        Order.objects.create(customer=self.customer1, order_date=now - timezone.timedelta(days=10), status="pending", total_amount=150.00)
        Order.objects.create(customer=self.customer2, order_date=now - timezone.timedelta(days=5), status="completed", total_amount=200.00)

    def test_top_customers(self):
        top_customers = Order.top_customers_last_6_months()
        
        # Print the output for debugging
        print("Top Customers:", top_customers)

        # Check if we have at least 2 customers
        self.assertGreaterEqual(len(top_customers), 2, "Not enough customers found.")

        # Check if Alice is in the results
        alice_found = any(
            customer['customer__name'] == 'Alice' and customer['total_spent'] == 250.00
            for customer in top_customers
        )
        self.assertTrue(alice_found, "Alice's total spent is not correct or is missing")

        # Check if Bob is in the results
        bob_found = any(
            customer['customer__name'] == 'Bob' and customer['total_spent'] == 200.00
            for customer in top_customers
        )
        self.assertTrue(bob_found, "Bob's total spent is not correct or is missing")
