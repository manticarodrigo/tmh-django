from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserAuthToken, UserViewSet, UserCreateViewSet, FacebookLogin, FacebookConnect
from .projects.views import ListProject, DetailProject

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'projects', ListProject)
router.register(r'projects', DetailProject)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # rest api
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', UserAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # fb auth
    re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
