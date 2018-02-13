from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer

from posts.models import Post 

class PostModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer()
	class Meta:
		model = Post
		fields = [
			'user',
			'content'
		]