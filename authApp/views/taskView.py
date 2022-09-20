from rest_framework import viewsets
from  authApp.models import Task
from authApp.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class TaskView(viewsets.ViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


    def list(self, request):
        serializer = TaskSerializer(self.queryset, many=True)
        return Response({'data':serializer.data})

    def retrieve(self, request,pk = None):
        task = get_object_or_404(Task, id =pk)
        serializer = TaskSerializer(task)
        return Response({'data': serializer.data})

    def create(self, request,pk =None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status = status.HTTP_201_CREATED )
        else:
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        task = get_object_or_404(Task, id =pk)
        task.delete()
        return Response({"task deleted"})
