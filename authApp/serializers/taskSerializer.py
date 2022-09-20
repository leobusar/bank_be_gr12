from rest_framework import serializers
from authApp.models  import Task
#from .userSerializer import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    #owner = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
        #fields = ['id', 'title', 'description', 'owner']
