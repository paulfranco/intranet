from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from posts.models import Post 

class ParentPostModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = [
			'id',
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',

		]


	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y | at %I:%M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago"

class PostModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent = ParentPostModelSerializer(read_only=True)

	class Meta:
		model = Post
		fields = [
			'id',
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',
			'parent'

		]



	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y | at %I:%M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago"