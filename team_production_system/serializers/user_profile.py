from rest_framework import serializers
from . import (
    CustomUserSerializer,
    MenteeProfileSerializer,
    MentorProfileSerializer,
    NotificationSettingsSerializer,
)


# Version 2 of the serializer for the user's profile information
class UserProfileSerializer(serializers.Serializer):
    my_profile = CustomUserSerializer()
    mentee_profile = MenteeProfileSerializer()
    mentor_profile = MentorProfileSerializer()
    notification_settings = NotificationSettingsSerializer()

    class Meta:
        fields = [
            'my_profile',
            'mentor_profile',
            'mentee_profile',
            'notification_settings',
        ]
