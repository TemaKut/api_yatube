from django.urls import path, include

from rest_framework.authtoken import views as v
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                views.PostCommentsViewSet, basename='comments')
router.register(r'groups', views.GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-token-auth/', v.obtain_auth_token),
]
