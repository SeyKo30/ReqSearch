import pytest
from django.contrib.auth.models import User
from main.forms import CompanyForm, SignUpForm, DocumentForm, TextInputForm
from main.models import Company, UploadedDocument
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture(autouse=True)
def clear_db(db):
    User.objects.all().delete()
    Company.objects.all().delete()
    UploadedDocument.objects.all().delete()

@pytest.mark.django_db
def test_company_form_valid_data():
    form = CompanyForm(data={
        'name': 'Test Company',
        'EDR': '1234567890',
        'responsible_person': 'John Doe',
        'phone_number': '123456789',
        'address': '123 Test St'
    })
    assert form.is_valid()
    company = form.save(commit=False)
    company.user = User.objects.create_user(username='testuser', password='12345')
    company.save()
    assert Company.objects.count() == 1

@pytest.mark.django_db
def test_company_form_invalid_data():
    form = CompanyForm(data={
        'name': '',
        'EDR': '1234567890',
        'responsible_person': 'John Doe',
        'phone_number': '123456789',
        'address': '123 Test St'
    })
    assert not form.is_valid()
    assert 'name' in form.errors

@pytest.mark.django_db
def test_signup_form_valid_data():
    form = SignUpForm(data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password1': 'strongpassword123',
        'password2': 'strongpassword123'
    })
    assert form.is_valid()
    user = form.save()
    assert User.objects.count() == 1
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'

@pytest.mark.django_db
def test_signup_form_invalid_data():
    form = SignUpForm(data={
        'username': 'testuser',
        'email': 'invalidemail',
        'password1': 'strongpassword123',
        'password2': 'differentpassword'
    })
    assert not form.is_valid()
    assert 'email' in form.errors
    assert 'password2' in form.errors

@pytest.mark.django_db
def test_document_form_valid_data():
    uploaded_file = SimpleUploadedFile('testfile.txt', b'This is the content of the file.')
    form = DocumentForm(data={}, files={'file': uploaded_file})
    assert form.is_valid()

def test_text_input_form_valid_data():
    form = TextInputForm(data={'text': 'This is a test.'})
    assert form.is_valid()

def test_text_input_form_invalid_data():
    form = TextInputForm(data={'text': ''})
    assert not form.is_valid()
    assert 'text' in form.errors
