from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    link_fb = models.URLField(max_length=128,
                              db_index=True,
                              blank=True)
    description = models.TextField(null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
