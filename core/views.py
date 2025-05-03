from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Marca
from .serializers import MarcaSerializer

class MarcaList(APIView):
    def get(self, request):
        marcas = Marca.objects.all()
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)
