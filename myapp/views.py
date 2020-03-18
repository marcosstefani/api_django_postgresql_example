from django.views.decorators.cache import cache_page
from .models import User
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from datetime import date, datetime

import itertools

@api_view(['GET','POST'])
def user_birthday(request):
    if request.method == 'GET':
        conditional = request.query_params.get('from', None) or request.query_params.get('to', None)
        if conditional:
            from_value = request.query_params.get('from', "01.01.1900")
            to_value = request.query_params.get('to', date.today().strftime("%d.%m.%Y"))
            users = User.objects.filter(birthday__range=[datetime.strptime(from_value, '%d.%m.%Y').date(), datetime.strptime(to_value, '%d.%m.%Y').date()])
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        valid = []
        errors = []
        for user in body:
            serializer = UserSerializer(data=user)
            if serializer.is_valid():
                valid.append(serializer)
            else:
              errors.append({"user": user, "alert": serializer.errors})

        if len(errors) == 0:
            for user in valid:
                user.save()
            return Response(body, status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

# Cache 1 hour
@cache_page(60 * 60)
@api_view(['GET'])
def user_birthday_sum(request):
    return Response(sum(abs(date.today().year - user.birthday.year - 
         ((date.today().month, date.today().day) < 
         (user.birthday.month, user.birthday.day))) for user in User.objects.all()))