from rest_framework import viewsets, mixins

# FB Views
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialConnectView

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer

class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    """
    Retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

# class UserUpdateViewSet(
#     mixins.UpdateModelMixin,
#     viewsets.GenericViewSet):
#     """
#     Updates user accounts
#     """
#     queryset = User.objects.all()
#     serializer_class = UpdateUserSerializer
#     permission_classes = (IsUserOrReadOnly,)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter