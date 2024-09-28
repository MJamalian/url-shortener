from django.shortcuts import get_object_or_404, redirect

import random

from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Url

import redis

from django.core.cache import cache

redis_instance = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

# Create your views here.

class GetShortUrlView(APIView):
    def get(self, request):
        long_link = request.query_params["link"]
        random_url = random.randint(0, 10000)
        while Url.objects.filter(short_link=random_url).exists():
            random_url = random.randint(0, 10000)

        Url.objects.create(long_link=long_link, short_link=str(random_url))
        return Response(f"{request.get_host()}/{random_url}")


class GetLongUrlView(APIView):
    def get(self, request, short_url):
        if short_url in cache:
            print("hello")
            return redirect(cache.get(short_url))

        url = get_object_or_404(Url, short_link=short_url)
        cache.set(short_url, url.long_link, 60*60)
        return redirect(url.long_link)

