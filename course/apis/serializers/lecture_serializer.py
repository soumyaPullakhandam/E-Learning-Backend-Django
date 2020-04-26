from rest_framework import serializers
from course.models import Lecture


class LectureSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.topic.author.username', read_only=True)
    author = serializers.CharField(source='course.topic.author.id', read_only=True)
    course_name = serializers.CharField(source='course', read_only=True)
    topic_name = serializers.CharField(source='topic', read_only=True)

    class Meta:
        model = Lecture
        fields = '__all__'
        read_only_fields = ['author', 'author_name', 'course_name', 'topic_name']
