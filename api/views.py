from django.shortcuts import render,HttpResponse 
from . models import Contact 

from .serializers import ContactSerializer,UserSerializer
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.

@csrf_exempt
def ContactView(request):
    if request.method =="GET":
        contactdata=Contact.objects.all()
        serializer=ContactSerializer(contactdata,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        jsoncontactdata = JSONParser().parse(request)
        print(jsoncontactdata)
   
        serializer = ContactSerializer(data=jsoncontactdata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.data,status=400)

@csrf_exempt
def ContactDetailView(request,pk):
    contactdata=Contact.objects.get(id=pk)
    if request.method=="DELETE":
        contactdata.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method =="GET":

            serializer=ContactSerializer(contactdata)
            return JsonResponse(serializer.data,safe=False)
    
    elif request.method =="PUT":
        jsoncontactdata = JSONParser().parse(request)
        print(jsoncontactdata)
        serializer=ContactSerializer(contactdata,data=jsoncontactdata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



def UserView(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return JsonResponse(serializer.data,safe=False)