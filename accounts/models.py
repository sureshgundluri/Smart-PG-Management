from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PG(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    pg_name = models.CharField(max_length=100)
    pg_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pg_name
