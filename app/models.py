from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Image(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'images/', default = 'images/no_image.jpg')