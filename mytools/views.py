from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import itertools

@api_view(['GET'])
def letter_digit(request):
    text = request.query_params.get('str', None)
    if text:
        return Response(set(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in text)))))
    return Response('text not found in str param', status=status.HTTP_400_BAD_REQUEST)
