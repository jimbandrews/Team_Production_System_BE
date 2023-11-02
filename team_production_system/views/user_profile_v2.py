from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team_production_system.serializers import UserProfileSerializer


class UserProfileV2(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user

        if not user.is_authenticated:
            return Response(
                {'error': 'User is not authenticated.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )
