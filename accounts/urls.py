from django.urls import path
from accounts. views import AuthorPost, AuthorPostDetail


app_name = 'accounts'

urlpatterns = [
 path('author-post/',AuthorPost.as_view()),
 path('author-post-detail/<int:pk>',AuthorPostDetail.as_view())
]
