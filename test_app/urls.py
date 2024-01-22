from django.urls import path
from . import views

app_name = 'test_app' # application namespace
urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('friend-request/', views.FriendRequestListView.as_view(), name='friend_request_list'),
    path('friend-request/create/', views.FriendRequestCreateView.as_view(), name='friend_request_create'),
    path('group/', views.GroupListView.as_view(), name='group_list'),
    path('group/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('group/create/', views.GroupCreateView.as_view(), name='group_create'),
    path('group/update/<int:pk>/', views.GroupUpdateView.as_view(), name='group_update'),
    path('message/', views.MessageListView.as_view(), name='message_list'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_create'),
]