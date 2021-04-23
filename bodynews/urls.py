from django.urls import path

from .views import (PostListView, post_detail, 
                    PostCreateView, delete_comment,
                    RulesView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('rules/', RulesView.as_view(), name='rules'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('<int:pk>/delete_comment/', delete_comment, name='comment_delete'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    
]


