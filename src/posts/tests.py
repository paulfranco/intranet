from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
from .models import Post

User = get_user_model()

class PostModelTestCase(TestCase):
	def setUp(self):
		some_random_user= User.objects.create(username='jmitchell')

	def test_post_item(self):
		obj = Post.objects.create(
				user = User.objects.first(),
				content = 'Some Random Content'

			)
		self.assertTrue(obj.content == 'Some Random Content')
		self.assertTrue(obj.id == 1)
		absolute_url = reverse('post:detail', kwargs={"pk": 1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)

	def test_post_url(self):
		obj = Post.objects.create(
			user = User.objects.first(),
			content = 'Some Random Content'
		)
		absolute_url = reverse('post:detail', kwargs={"pk": obj.pk})
		self.assertEqual(obj.get_absolute_url(), absolute_url)