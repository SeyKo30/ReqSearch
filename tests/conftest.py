import pytest
import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'TenWeb.settings'
django.setup()


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
