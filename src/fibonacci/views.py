from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

import json
from fibonacci.gRPC.client import main
from fibonacci.MQTT.publisher import send

# Create your views here.
class EchoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        order = json.loads(request.body)['order']
        # print(order)
        send(order)
        ans = main({ "ip": "localhost", "port": 8080, "order": order})
        return Response(data = {"order": order, "answer": ans}, status = 200)

    # def get(self, request):

    #     ans = main({ "ip": "localhost", "port": 8080, "order": 10})
    #     return Response(data = {"order": 10, "answer": ans}, status = 200)

