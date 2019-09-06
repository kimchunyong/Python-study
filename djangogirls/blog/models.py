from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True,null=True)

    def publish(self):
        slef.publised_data = timezone.now()
        slef.save()

    def __str__(self):
        return self.title
