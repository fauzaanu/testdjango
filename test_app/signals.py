from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile, Post, FriendRequest, Group, GroupMembership, Message

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Post)
def update_post_count(sender, instance, created, **kwargs):
    """
    Update the post count in the author's profile when a new post is created.
    """
    if created:
        author_profile = instance.user.profile
        author_profile.post_count += 1
        author_profile.save()

@receiver(post_delete, sender=Post)
def decrease_post_count(sender, instance, **kwargs):
    """
    Decrease the post count in the author's profile when a post is deleted.
    """
    author_profile = instance.user.profile
    author_profile.post_count -= 1
    author_profile.save()

@receiver(post_save, sender=FriendRequest)
def update_friend_request(sender, instance, created, **kwargs):
    """
    Update the friend requests status.
    """
    if created:
        sender_profile = instance.sender.profile
        sender_profile.sent_friend_requests.add(instance)
        sender_profile.save()

        receiver_profile = instance.receiver.profile
        receiver_profile.received_friend_requests.add(instance)
        receiver_profile.save()

@receiver(post_delete, sender=FriendRequest)
def delete_friend_request(sender, instance, **kwargs):
    """
    Delete the friend request.
    """
    sender_profile = instance.sender.profile
    sender_profile.sent_friend_requests.remove(instance)
    sender_profile.save()

    receiver_profile = instance.receiver.profile
    receiver_profile.received_friend_requests.remove(instance)
    receiver_profile.save()

@receiver(post_save, sender=GroupMembership)
def update_group_membership(sender, instance, created, **kwargs):
    """
    Add the user to the group.
    """
    if created:
        group = instance.group
        group.members.add(instance.user)
        group.save()

@receiver(post_delete, sender=GroupMembership)
def remove_group_membership(sender, instance, **kwargs):
    """
    Remove the user from the group.
    """
    group = instance.group
    group.members.remove(instance.user)
    group.save()

@receiver(post_save, sender=Message)
def update_message(sender, instance, created, **kwargs):
    """
    Update the sender and receiver's messages.
    """
    if created:
        sender_profile = instance.sender.profile
        sender_profile.sent_messages.add(instance)
        sender_profile.save()

        receiver_profile = instance.receiver.profile
        receiver_profile.received_messages.add(instance)
        receiver_profile.save()

@receiver(post_delete, sender=Message)
def delete_message(sender, instance, **kwargs):
    """
    Delete the message from the sender and receiver's messages.
    """
    sender_profile = instance.sender.profile
    sender_profile.sent_messages.remove(instance)
    sender_profile.save()

    receiver_profile = instance.receiver.profile
    receiver_profile.received_messages.remove(instance)
    receiver_profile.save()
   
# NOTES TO DEVELOPER:       
# [NOTE] Added signals for the FriendRequest, GroupMembership, and Message models. 
# [NOTE] Updated instances of "author" to "user" in the post signals.  
# [NOTE] Updated the sender and receiver fields in the Message model signals.