from django.urls import include

from rest_framework.authtoken import views as v
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'apiv1'

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                views.PostCommentsViewSet, basename='post-comments')
router.register(r'groups', views.GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', v.obtain_auth_token),
]
