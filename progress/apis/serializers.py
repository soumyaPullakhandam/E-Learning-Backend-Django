from rest_framework import serializers
from ..models import Progress


class ProgressSerializers(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    lecture_name = serializers.CharField(source='lecture', read_only=True)
    topic_name = serializers.CharField(source='lecture.topic', read_only=True)
    course_name = serializers.CharField(source='lecture.topic.course', read_only=True)
    duration = serializers.FloatField(source='lecture.duration', read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'student', 'student_name', 'course_name', 'topic_name', 'lecture', 'lecture_name', 'duration',
                  'completion',
                  'timestamp']
        read_only_fields = ['student', 'student_name', 'lecture_name', 'lecture']
