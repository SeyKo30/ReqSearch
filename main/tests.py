from django.test import TestCase
from .models import Company
from django.contrib.auth.models import User

class CompanyTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_company_creation(self):

        company = Company.objects.create(
            user=self.user,
            name='Test Company',
            EDR='1234567890',
            phone_number='123-456-7890',
            address='123 Test St, Test City',
            responsible_person='John Doe'
        )


        self.assertEqual(company.user, self.user)
        self.assertEqual(company.name, 'Test Company')
        self.assertEqual(company.EDR, '1234567890')
        self.assertEqual(company.phone_number, '123-456-7890')
        self.assertEqual(company.address, '123 Test St, Test City')
        self.assertEqual(company.responsible_person, 'John Doe')

class SimpleTestCase(TestCase):
    def test_simple(self):
        self.assertTrue(True)
