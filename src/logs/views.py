from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from logs.gRPC.client import main

# Create your views here.
class EchoView(APIView):
    permission_classes = (permissions.AllowAny,)

    # def post(self, request):

    #     order = json.loads(request.body)['order']
    #     # print(order)
    #     ans = main({ "ip": "localhost", "port": 8080, "order": order})
    #     return Response(data = {"order": order, "answer": ans}, status = 200)

    def get(self, request):

        history = main({ "ip": "localhost", "port": 8800})
        return Response(data = {"history": history[:]}, status = 200)

