from django.db import models

class UserLocation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    # New avatar field; files will be stored under media/avatars/
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    lat = models.FloatField()
    lon = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
