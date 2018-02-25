from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from .validators import validate_content

# def validate_content(value):
# 	content = value
# 	if content == "abc":
# 		raise ValidationError("Content cannot be abc")
# 	return value
class PostManager(models.Manager):
	def repost(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else: 
			og_parent = parent_obj
		qs = self.get_queryset().filter(
				user=user, parent=og_parent
				).filter(
					timestamp__year=timezone.now().year,
					timestamp__month=timezone.now().month,
					timestamp__day=timezone.now().day,

				)
		if qs.exists():
			return None

		obj = self.model(
				parent = parent_obj,
				user = user,
				content = parent_obj.content, 
			)
		obj.save()

		return obj

class Post(models.Model):
	parent		= models.ForeignKey("self", blank=True, null=True)
	user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.CharField(max_length=240, validators = [validate_content])
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = PostManager()

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("post:detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ['-timestamp']


	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc"
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Post, self).clean(*args, **kwargs)

