from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class user(models.Model):
    username = models.CharField(_("Username"), max_length=100)
    email = models.EmailField(_("Email Id"), max_length=254)

    def __str__(self):
        return f"{self.username}"