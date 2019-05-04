from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from tmh.api.user.views import UserViewSet, FacebookLogin, FacebookConnect
from tmh.api.project.views import ProjectViewSet
from tmh.api.detail.views import ProjectDetailViewSet
from tmh.api.item.views import ProjectItemViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'details', ProjectDetailViewSet)
router.register(r'items', ProjectItemViewSet)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # rest api
    path('api/v1/', include(router.urls)),

    # rest-auth
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),
    re_path(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
