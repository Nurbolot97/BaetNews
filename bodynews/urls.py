from django.urls import path
from .views import post_list, post_detail, new_post, delete_comment


urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/delete_comment/', delete_comment, name='comment_delete'),
    path('new_post/', new_post, name='new_post'),
    
]


