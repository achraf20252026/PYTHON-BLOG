from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    auteur=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    titre=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        return self.titre