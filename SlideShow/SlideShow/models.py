from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to="images")
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=False)

	class Meta:
		ordering = ['-publish']

	def __str__(self):
		return self.title


class SlideShow(models.Model):
	article = models.OneToOneField(Article, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)

	class Meta:
		ordering = ['-article__publish']

	def __str__(self):
		return self.article.title