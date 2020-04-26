from rest_framework import serializers
from course.models import Topic


class TopicSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.author.username', read_only=True)
    author = serializers.IntegerField(source='course.author.id', read_only=True)
    course_name = serializers.CharField(source='course', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
