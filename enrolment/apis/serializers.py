from rest_framework import serializers
from ..models import Enrolment
from course.apis.serializers import CourseListSerializers


class EnrolmentSerializers(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    course_name = serializers.CharField(source='course', required=False, read_only=True)
    course_list = CourseListSerializers(source='course', many=False, read_only=True)

    class Meta:
        model = Enrolment
        fields = '__all__'
        read_only_fields = ['student', 'student_name', 'course_name', 'completion', 'rating']


class EnrolmentUpdateSerializers(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    course_name = serializers.CharField(source='course', required=False, read_only=True)
    course_list = CourseListSerializers(many=False)

    class Meta:
        model = Enrolment
        fields = '__all__'
        read_only_fields = ['student', 'student_name', 'course_name', 'completion', 'course']
