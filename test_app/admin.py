from django.contrib import admin
from .models import Profile, Post, FriendRequest, Group, GroupMembership, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_picture', 'bio', 'contact_information']


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'timestamp']


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'status']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'creator', 'timestamp']


class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'group']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'content', 'timestamp']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMembership, GroupMembershipAdmin)
admin.site.register(Message, MessageAdmin)
