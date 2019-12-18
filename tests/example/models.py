from django.db import models


class ModelForTesting(models.Model):
    """Mixin class for models used in testing."""

    class Meta:
        app_label = "example"
        abstract = True


class Simple(ModelForTesting):
    name = models.CharField(max_length=128)
