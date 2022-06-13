from django.urls import path

from posts.views import PostDetail, PostList

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("post-detail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
]
