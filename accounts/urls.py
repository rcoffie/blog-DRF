from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import (
    AddCategoryView,
    AuthorPost,
    AuthorPostDetail,
    CreatePostView,
    logout_view,
    registration_view,
)

app_name = "accounts"

urlpatterns = [
    path("author-post/", AuthorPost.as_view()),
    path("author-post-detail/<int:pk>", AuthorPostDetail.as_view()),
    path("login/", obtain_auth_token, name="login"),
    # path('register/',RegisterView.as_view()),
    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("create-post/", CreatePostView.as_view()),
    path("add-category/", AddCategoryView.as_view(), name="add-category"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
