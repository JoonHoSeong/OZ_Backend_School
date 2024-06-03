from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializer

class Feeds(APIView):
    #전체 계시글 조회
    
    def get(self, request) :
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid() :
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        

        # return Response(serializer.errors, status=400)
    
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try :
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id) :
        feed = self.get_object(feed_id)
        serializer = FeedSerializer(feed)
        return Response(serializer.data)
    