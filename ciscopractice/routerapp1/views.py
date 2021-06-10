import json
from django.shortcuts import render


from .models import RouterDetails
from .serializer import RouterDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.http import HttpResponse

class RouterDetail(APIView):
    print("Inside APIView")
    #permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        import requests
        queryset = RouterDetails.objects.filter().order_by("-id")
        data=RouterDetails.objects.values_list('hostname', flat = True).order_by("-id")
        response = requests.get(data[0])
        data1={'payload':response.json()}
        #for i in data:
        print(data)
        # r = requests.post('https://google.com', json={"key": "value"})
        # print(r)

        return HttpResponse(json.dumps(data1), content_type="application/json")




class AddData(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add.html'

    def get(self, request):
        return Response({'message' : 'Add new data'})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        #print(data['hostname'],'-----------')
        import requests

        response = requests.get(data['hostname'])
        data1={'payload':response.json()}
        data2={'payload':data1}
        print(data2)
        #data1={'payload':'Naik'}
        data.update(data1)
        # print(data)
        # print('========================')
        serializer = RouterDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Record inserted successfully'}, status=status.HTTP_200_OK)
        return Response({'message' : 'Record cannot be added'})










def info(request):
    helpdict = {'data':{'Receiver':'Cisco is the best!'}}

    return render(request,'help.html',context=helpdict)
