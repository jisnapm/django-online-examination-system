from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import QuestionDb
from ExamApp.serializers import QuestionSerializer

# Create your views here.
class QuestionListCreate(APIView):
    def get(self, request):
        qs = QuestionDb.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(data = serializer_instance.data)

    def post(self, request):
        form_data = request.data
        s_instance = QuestionSerializer(data=form_data)
        if s_instance.is_valid():
            actual_data = s_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data = {"message": "Question created successfully"})
        else:
            return Response(data = s_instance.errors)

class QuestionRetreiveUpdateDelete(APIView):
    def get(self, request, pk):
        qs = QuestionDb.objects.get(id = pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data = serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        s_instance = QuestionSerializer(data= form_data)
        if s_instance.is_valid():
            actual_data = s_instance.validated_data
            QuestionDb.objects.filter(id = pk).update(**actual_data)
            return Response(data = s_instance.data)
        else:
            return Response(data= s_instance.errors)

    def delete(self, request, pk):
        QuestionDb.objects.filter(id = pk).delete()
        return Response(data= {"message": "Question Deleted!"})