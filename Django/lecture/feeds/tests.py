from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User

class FeedAPITestCase(APITestCase):
    def setup(self) :
        self.user = User.objects.create_user(username = 'test', password = '123')
        
        self.feed1 = Feed.objects.create(User = self.user, title='test title', content = 'test content')
        self.feed2 = Feed.objects.create(User = self.user, title='test title2', content = 'test content')
        
    def test_get_all_feeds(self):
        url = reverse('all_feeds')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.content), 2)
        
    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id' : 1})
        # res = self.client.get(url)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(len(res.content),2)