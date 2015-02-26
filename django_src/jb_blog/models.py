from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	published = models.BooleanField(default=False)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, unique=True, blank=True)
	abstract = RichTextField()
	content = RichTextField()
	created = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(unicode(self.title))
		super(Post, self).save(*args, **kwargs)

	def publish(self): 
		"""
		Publish or Un_publish Post.
		"""
		if self.published == True:
			self.published = False
			self.published_date = None
			self.save()
		else:
			self.published = True
			self.published_date = timezone.now()
			self.save()

	def get_absolute_url(self):
		return "/blog/post/%s/" % (self.slug)

	def __str__(self): 
		return self.title

