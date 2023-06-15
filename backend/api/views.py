from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import requests
import json
class Greeting(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        content = {'greeting': 'Hello, World!'}
        return Response(content)

@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
    })

class Ensembl(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, ensid,format=None):
        r = requests.get('https://rest.ensembl.org/lookup/id/'+ensid+'?content-type=application/json')
        if not r.ok:
            data = {"ensid": ensid, "data": "None"}
        else:
            data = r.json()
        return Response(data)
