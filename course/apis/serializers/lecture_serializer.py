from rest_framework import serializers
from course.models import Lecture, LectureFile


class LectureSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.topic.author.username', read_only=True)
    author = serializers.CharField(source='course.topic.author.id', read_only=True)
    course_name = serializers.CharField(source='course', read_only=True)
    topic_name = serializers.CharField(source='topic', read_only=True)
    file_url = serializers.FileField(source='lectureFile.lecture_file', read_only=True)

    class Meta:
        model = Lecture
        fields = '__all__'
        read_only_fields = ['author', 'author_name', 'course_name', 'topic_name']


class LectureFileSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='course.topic.author.id', read_only=True)
    course_name = serializers.CharField(source='course', read_only=True)
    topic_name = serializers.CharField(source='topic', read_only=True)
    lecture_file = serializers.ListField(write_only=True,
                                         child=serializers.FileField(max_length=100000, allow_empty_file=False,
                                                                     use_url=False, write_only=True)
                                         )

    class Meta:
        model = LectureFile
        fields = ['id', 'lecture_file', 'file', 'author', 'topic', 'topic_name', 'course_name', 'course']

    def create(self, validated_data):
        lecture_files = validated_data.pop('lecture_file')
        for lecture_file in lecture_files:
            lecture_file = LectureFile.objects.create(file=lecture_file, **validated_data)
        return lecture_file


