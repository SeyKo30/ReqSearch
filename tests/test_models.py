import pytest
from django.contrib.auth.models import User
from main.models import Company, UploadedDocument

@pytest.mark.django_db
def test_company_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    company = Company.objects.create(
        user=user,
        name='Test Company',
        EDR='1234567890',
        phone_number='123456789',
        address='123 Test St',
        responsible_person='John Doe'
    )
    assert company.name == 'Test Company'
    assert company.EDR == '1234567890'
    assert company.phone_number == '123456789'
    assert company.address == '123 Test St'
    assert company.responsible_person == 'John Doe'

@pytest.mark.django_db
def test_uploaded_document_creation():
    document = UploadedDocument.objects.create(
        file='documents/2023/01/01/testfile.txt'
    )
    assert document.file == 'documents/2023/01/01/testfile.txt'
