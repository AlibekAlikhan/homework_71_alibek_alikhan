from django.urls import path

from accounts.views import logout_view
from api.views.posts_api_view import like_api
from posts.views import PostsView, PostsCreateView, PostsProfileView, CommentView, LikeView, SubscriptionsView, CommentDetailView

urlpatterns =[
    path('', PostsView.as_view(), name='index'),
    path('comment/<int:pk>', CommentView.as_view(), name="to_comment"),
    path('post/create', PostsCreateView.as_view(), name='post_create'),
    path('logout/', logout_view, name='logout'),
    # path('like/<int:pk>', LikeView.as_view(), name='like'),
    path('like/<int:pk>', like_api, name='like'),
    path('subscriptions/<int:pk>', SubscriptionsView.as_view(), name='subscriptions'),
    path('post/comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
]