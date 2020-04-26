from rest_framework import serializers
from course.models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    language_name = serializers.CharField(source='get_language_display', required=False, read_only=True)

    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['author', 'author_name', 'language_name', 'duration', 'rating']


class CourseListSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    language_name = serializers.CharField(source='get_language_display', required=False, read_only=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['author', 'author_name', 'language_name', 'duration', 'rating']

# from rest_framework.serializers import ModelSerializer, RelatedField
# class CategoryRelatedField(serializers.RelatedField):
#     def to_representation(self, obj):
#         data = {
#             'id': obj.id,
#             'title': obj.title
#         }
#         return data
#
#     def to_internal_value(self, id):
#         return Category.objects.get(id=id)

# category = CategoryRelatedField(
#     queryset=Category.objects.all(), many=True, required=True
# )


# def create(self, validated_data):
#     category_data = validated_data.pop('category')
#     course = Course.objects.create(**validated_data)
#     for cat in category_data:
#         C = Category.save(**cat)
#         course.category.add(C)
#     return course
