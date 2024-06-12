from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feeds.as_view(), name = 'all_feeds'),
    path('<int:feed_id>', views.FeedDetail.as_view(), name = 'feed_detail'),
]