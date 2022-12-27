from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from djangotestapp.models import user
from djangotestapp.serilaizer import UserSerailizer

class UserView(APIView):

    def get(self,request):
        users = user.objects.all()
        serializer = UserSerailizer(users)
        return Response(serializer.data)

    def post(self,requset):
        serilaizer = UserSerailizer(data=requset.data)
        if serilaizer.is_valid():
            try:
                serilaizer.save()
                return Response(serilaizer.data)
            except:
                return Response("Something bad Occurs")
        return Response("Check Seraializer")