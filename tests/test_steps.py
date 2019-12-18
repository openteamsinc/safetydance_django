from django.urls import reverse
from safetydance_django.steps import *
from safetydance_test import scripted_test
import pytest


@pytest.mark.django_db
@scripted_test
def test_get():
    get(reverse('simple-list'))
    status_code_is(200)
