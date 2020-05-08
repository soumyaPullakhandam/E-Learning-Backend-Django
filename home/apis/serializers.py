from rest_framework import serializers

from ..models import UserProfile, Languages


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'groups', 'first_name', 'last_name', 'biography', 'website',
                  'qualification', 'phone', 'id']
        # fields = '__all__'
        # read_only_fields = ['password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LanguageSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='get_language_display', required=False, read_only=True)

    class Meta:
        model = Languages
        fields = '__all__'
