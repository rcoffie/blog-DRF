from django.urls import path

from posts.views import CreateComment, PostCommentList, PostDetail, PostList

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("post-detail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("create-post/<int:pk>/comment/",CreateComment.as_view(),name="create_post-comment"),
    path("post/<int:pk>/comment/", PostCommentList.as_view(), name="post-comment-list"),
]
