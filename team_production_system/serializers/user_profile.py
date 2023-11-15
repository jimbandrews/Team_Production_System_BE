from rest_framework import serializers

from team_production_system.models import CustomUser

from . import (
    MenteeProfileSerializer,
    MentorProfileSerializer,
    NotificationSettingsSerializer,
    SessionSerializer,
)


# Version 2 of the serializer for the user's profile information
class UserProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()
    mentor_info = MentorProfileSerializer(read_only=True, source='mentor')
    mentee_info = MenteeProfileSerializer(read_only=True, source='mentee')
    notification_settings = NotificationSettingsSerializer(read_only=True)
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'pk',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile_photo',
            'is_mentor',
            'is_mentee',
            'is_active',
            'mentee_info',
            'mentor_info',
            'notification_settings',
            'sessions',
        ]
