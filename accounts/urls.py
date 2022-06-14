from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import AuthorPost, AuthorPostDetail, logout_view, registration_view, CreatePostView, AddCategoryView

app_name = "accounts"

urlpatterns = [
    path("author-post/", AuthorPost.as_view()),
    path("author-post-detail/<int:pk>", AuthorPostDetail.as_view()),
    path("login/", obtain_auth_token, name="login"),
    # path('register/',RegisterView.as_view()),
    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("create-post/",CreatePostView.as_view()),
    path('add-category/', AddCategoryView.as_view(), name='add-category')
]
