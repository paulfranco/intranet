from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post 
from posts.api.pagination import StandardResultsPagination
from posts.api.serializers import PostModelSerializer

from hashtags.models import HashTags

class TagPostAPIView(generics.ListAPIView):
	queryset = Post.objects.all().order_by("-timestamp")
	serializer_class = PostModelSerializer
	pagination_class = StandardResultsPagination

	def get_serialiser_context(self, *args, **kwargs):
		context = super(TagPostAPIView, self).get_serialiser_context(*args, **kwargs)
		context['request'] = self.request
		return context

	def get_queryset(self, *args, **kwargs):
		hashtag = self.kwargs.get("hashtag")
		hashtag_obj = None
		try:
			hashtag_obj = HashTags.objects.get_or_create(tag=hashtag)[0]
		except:
			pass
		if hashtag_obj:
			qs = hashtag_obj.get_posts()
			query = self.request.GET.get("q", None)
			if query is not None:
				qs = qs.filter(
						Q(content__icontains=query) |
						Q(user__username__icontains=query)
						)
			return qs 
		return None

