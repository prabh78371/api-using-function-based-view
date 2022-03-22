from django.shortcuts import render
import io
from itsdangerous import Serializer
from rest_framework.parsers import JSONParser
from .serializer import studentserializer
from .models import student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def stu_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serilizer = studentserializer(data = python_data)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg':"created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data)

    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serilizer = studentserializer(data = python_data)
        id = python_data.get('id',None)
        if id is not None:
            stu = student.objects.get(id=id)
            serilizer = studentserializer(stu)
            json_data = JSONRenderer().render(serilizer.data)
            return HttpResponse(json_data)
        stu = student.objects.all()
        serilizer = studentserializer(stu ,many=True)
        json_data = JSONRenderer().render(serilizer.data)
        return HttpResponse(json_data)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = student.objects.get(id=id)
        serilizer = studentserializer(stu,data =python_data,partial =True)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg':'updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        return JsonResponse(res,safe = False)