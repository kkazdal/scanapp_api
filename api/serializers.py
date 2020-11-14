from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields =('id',  'photo')

	def get_photo_url(self, task):
		request = self.context.get('request')
		photo_url = task.photo.url

		return request.build_absolute_uri(photo_url)

class Base64Serializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'base64Text')

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields =('id',  'photo')


