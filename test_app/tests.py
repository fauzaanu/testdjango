from django.test import TestCase
from .models import Profile, Post, FriendRequest, Group, Message


class ProfileDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(name='Test Profile', bio='Test bio', contact_information='Test contact info')

    def test_template_used(self):
        response = self.client.get('/profile/1/')
        self.assertTemplateUsed(response, 'test_app/profile_detail.html')

    def test_context_object_name(self):
        response = self.client.get('/profile/1/')
        self.assertEqual(response.context['profile'].name, 'Test Profile')


class ProfileUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(name='Test Profile', bio='Test bio', contact_information='Test contact info')

    def test_template_used(self):
        response = self.client.get('/profile/1/update/')
        self.assertTemplateUsed(response, 'test_app/profile_update.html')

    def test_fields(self):
        response = self.client.get('/profile/1/update/')
        self.assertEqual(response.context['form'].fields.keys(), ['profile_picture', 'bio', 'contact_information'])


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test Post 1', content='Test content')
        Post.objects.create(title='Test Post 2', content='Test content')

    def test_template_used(self):
        response = self.client.get('/post/')
        self.assertTemplateUsed(response, 'test_app/post_list.html')

    def test_context_object_name(self):
        response = self.client.get('/post/')
        self.assertEqual(len(response.context['posts']), 2)


class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test Post', content='Test content')

    def test_template_used(self):
        response = self.client.get('/post/1/')
        self.assertTemplateUsed(response, 'test_app/post_detail.html')

    def test_context_object_name(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.context['post'].title, 'Test Post')


class FriendRequestListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        FriendRequest.objects.create(sender='Sender', receiver='Receiver')

    def test_template_used(self):
        response = self.client.get('/friend-request/')
        self.assertTemplateUsed(response, 'test_app/friend_request_list.html')

    def test_context_object_name(self):
        response = self.client.get('/friend-request/')
        self.assertEqual(len(response.context['friend_requests']), 1)


class FriendRequestCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        FriendRequest.objects.create(sender='Sender', receiver='Receiver')

    def test_template_used(self):
        response = self.client.get('/friend-request/create/')
        self.assertTemplateUsed(response, 'test_app/friend_request_create.html')

    def test_fields(self):
        response = self.client.get('/friend-request/create/')
        self.assertEqual(response.context['form'].fields.keys(), ['receiver'])


class GroupListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Test Group 1', description='Test description')
        Group.objects.create(name='Test Group 2', description='Test description')

    def test_template_used(self):
        response = self.client.get('/group/')
        self.assertTemplateUsed(response, 'test_app/group_list.html')

    def test_context_object_name(self):
        response = self.client.get('/group/')
        self.assertEqual(len(response.context['groups']), 2)


class GroupDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Test Group', description='Test description')

    def test_template_used(self):
        response = self.client.get('/group/1/')
        self.assertTemplateUsed(response, 'test_app/group_detail.html')

    def test_context_object_name(self):
        response = self.client.get('/group/1/')
        self.assertEqual(response.context['group'].name, 'Test Group')


class GroupCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Test Group', description='Test description')

    def test_template_used(self):
        response = self.client.get('/group/create/')
        self.assertTemplateUsed(response, 'test_app/group_create.html')

    def test_fields(self):
        response = self.client.get('/group/create/')
        self.assertEqual(response.context['form'].fields.keys(), ['name', 'description'])


class GroupUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Test Group', description='Test description')

    def test_template_used(self):
        response = self.client.get('/group/1/update/')
        self.assertTemplateUsed(response, 'test_app/group_update.html')

    def test_fields(self):
        response = self.client.get('/group/1/update/')
        self.assertEqual(response.context['form'].fields.keys(), ['name', 'description'])


class MessageListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Message.objects.create(sender='Sender', receiver='Receiver', content='Test message')

    def test_template_used(self):
        response = self.client.get('/message/')
        self.assertTemplateUsed(response, 'test_app/message_list.html')

    def test_context_object_name(self):
        response = self.client.get('/message/')
        self.assertEqual(len(response.context['messages']), 1)


class MessageCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Message.objects.create(sender='Sender', receiver='Receiver', content='Test message')

    def test_template_used(self):
        response = self.client.get('/message/create/')
        self.assertTemplateUsed(response, 'test_app/message_create.html')

    def test_fields(self):
        response = self.client.get('/message/create/')
        self.assertEqual(response.context['form'].fields.keys(), ['receiver', 'content'])
