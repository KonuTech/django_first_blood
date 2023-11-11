from django.urls import path
from . import views

app_name="posts"
urlpatterns = [
    path("posts/", views.posts_list, name="list"),
    path("posts/<int:id>", views.post_detail, name="detail"),
]
