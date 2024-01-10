from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import pdb

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_world(request):
    try:
        print('hola, mundo')
        return Response('Este es el responde del api')
    except:
        print('adios, mundo')
        return Response(status.HTTP_400_BAD_REQUEST)
    
