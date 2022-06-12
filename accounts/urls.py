from django.urls import path
from accounts. views import AuthorPost, AuthorPostDetail, registration_view, logout_view
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'accounts'

urlpatterns = [
 path('author-post/',AuthorPost.as_view()),
 path('author-post-detail/<int:pk>',AuthorPostDetail.as_view()),
 path('login/',obtain_auth_token, name='login'),
 # path('register/',RegisterView.as_view()),
 path('register/',registration_view,name='register'),
 path('logout/',logout_view,name='logout')
]
