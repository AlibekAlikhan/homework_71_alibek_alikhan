from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views.posts_api_view import PostSimpleView, like_api

router = routers.DefaultRouter()
router.register("posts", PostSimpleView)

urlpatterns =[
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name="obtain_auth_token"),
]
