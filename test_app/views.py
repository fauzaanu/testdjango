from django.views import generic
from .models import Profile, Post, FriendRequest, Group, Message

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'test_app/profile_detail.html'
    context_object_name = 'profile'

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = 'test_app/profile_update.html'
    fields = ['profile_picture', 'bio', 'contact_information']

class PostListView(generic.ListView):
    model = Post
    template_name = 'test_app/post_list.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'test_app/post_detail.html'
    context_object_name = 'post'

class FriendRequestListView(generic.ListView):
    model = FriendRequest
    template_name = 'test_app/friend_request_list.html'
    context_object_name = 'friend_requests'

class FriendRequestCreateView(generic.CreateView):
    model = FriendRequest
    template_name = 'test_app/friend_request_create.html'
    fields = ['receiver']

class GroupListView(generic.ListView):
    model = Group
    template_name = 'test_app/group_list.html'
    context_object_name = 'groups'

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'test_app/group_detail.html'
    context_object_name = 'group'

class GroupCreateView(generic.CreateView):
    model = Group
    template_name = 'test_app/group_create.html'
    fields = ['name', 'description']

class GroupUpdateView(generic.UpdateView):
    model = Group
    template_name = 'test_app/group_update.html'
    fields = ['name', 'description']

class MessageListView(generic.ListView):
    model = Message
    template_name = 'test_app/message_list.html'
    context_object_name = 'messages'

class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'test_app/message_create.html'
    fields = ['receiver', 'content']