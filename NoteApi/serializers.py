from rest_framework import fields, serializers
from .models import *
class NoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = "__all__"
