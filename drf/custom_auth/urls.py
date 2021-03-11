from custom_auth.views import UserViewSet, UserRoleViewSet
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('roles', UserRoleViewSet)

app_name = 'auth'
urlpatterns = [
    path('', include(router.urls)),
]
