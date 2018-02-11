from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_content

# def validate_content(value):
# 	content = value
# 	if content == "abc":
# 		raise ValidationError("Content cannot be abc")
# 	return value


class Post(models.Model):
	# user
	user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.CharField(max_length=240, validators = [validate_content])
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)


	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc"
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Post, self).clean(*args, **kwargs)
