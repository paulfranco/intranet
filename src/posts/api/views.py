from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView 
from rest_framework.response import Response 

from posts.models import Post 

from .pagination import StandardResultsPagination
from .serializers import PostModelSerializer

class RepostAPIView(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, pk, format=None):
		post_qs = Post.objects.filter(pk=pk)
		message = "Not Allowed"
		if post_qs.exists() and post_qs.count() == 1:
			# if request.user.is_authenticated():
			new_post = Post.objects.repost(request.user, post_qs.first())
			if new_post is not None:
				data = PostModelSerializer(new_post).data
				return Response(data)
			message = "Cannot repost the same in 1 day"
		return Response({ "message": message }, status=400)

class PostCreateAPIView(generics.CreateAPIView):
	serializer_class = PostModelSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class PostListAPIView(generics.ListAPIView):
	serializer_class = PostModelSerializer
	pagination_class = StandardResultsPagination


	def get_queryset(self, *args, **kwargs):
		im_following = self.request.user.profile.get_following()
		qs1 = Post.objects.filter(user__in=im_following).order_by("-timestamp")
		qs2 = Post.objects.filter(user=self.request.user)
		qs =  (qs1 | qs2).distinct().order_by("-timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | 
				Q(user__username__icontains=query)
				)
		return qs


class SearchAPIView(generics.ListAPIView):
	serializer_class = PostModelSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self, *args, **kwargs):
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | 
				Q(user__username__icontains=query)
				)
		return qs
