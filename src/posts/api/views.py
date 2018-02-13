from rest_framework import generics

from posts.models import Post 
from .serializers import PostModelSerializer

class PostListAPIView(generics.ListAPIView):
	serializer_class = PostModelSerializer


	def get_queryset(self):
		return Post.objects.all()
