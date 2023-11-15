from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from team_production_system.models import CustomUser
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

        try:
            return user
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {'error': 'An unexpected error occurred.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
