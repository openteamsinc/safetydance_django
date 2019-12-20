from django.urls import reverse
from safetydance_django.test import *
from safetydance_test import scripted_test, Given, When, Then, And
import pytest

@pytest.mark.django_db
@scripted_test
def test_get():
    Given.http.get(reverse('simple-list'))
    Then.http.status_code_is(200)
