from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import rest

router = DefaultRouter()
router.register(r"simple", rest.SimpleViewSet)
router.register(r"users", rest.UserViewSet)
schema_view = get_schema_view("Test safetydance_django API")

urlpatterns = [
    url(r"^api/", include(router.urls), name="api"),
    url(r"^api/schema", schema_view, name="api-schema"),
    url(
        r"^api/rest-framework/auth",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
