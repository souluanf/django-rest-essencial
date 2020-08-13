from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos da Geek
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'msg': 'Criou com sucesso'}, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliacões da Geek
    """

    def get(self, request):
        avaliacaoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacaoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
