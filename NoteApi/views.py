from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class ListNoteAPIView(ListAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer
    def get(self, request):
        notes = NoteModel.objects.all()
        serializer = NoteModelSerializer(notes, many=True)
        return Response({'status':status.HTTP_200_OK==200 if True else False,'notes':serializer.data})

class CreateNoteAPIView(CreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer
    def post(self, request):
        serializer = NoteModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = ""
            if status.HTTP_201_CREATED == 201:
                message = "Not başarıyla eklendi."
            else:
                message = "Not eklenirken bir sorun oluştu."
            return Response({'status':status.HTTP_201_CREATED == 201 if True else False,'message' : message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateNoteAPIView(UpdateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer

class DeleteNoteAPIView(DestroyAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer
    def get_object(self, pk):  
        return NoteModel.objects.get(pk=pk)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        message = ""
        if status.HTTP_200_OK == 200:
            message = "Not başarıyla silindi."
            snippet.delete()
        else:
            message = "Not silinirken bir sorun oluştu."
        return Response({'status':status.HTTP_200_OK == 200 if True else False,'message' : message}, status=status.HTTP_200_OK)