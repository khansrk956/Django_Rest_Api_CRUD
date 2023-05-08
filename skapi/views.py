from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from . models import Student
from . serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method=="GET":
        # data comes from client side in json form.
        json_data = request.body
        # data push in stream to convert into byte form 0 and 1.
        stream = io.BytesIO(json_data)
        # convert stream data finally into python data which is in dic form.
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            # The data come from database in stu variable and convert into the complex form(means row form inside the table.)
            serializer = StudentSerializer(stu)
            # convert python data into json data.
            json_data = JSONRenderer().render(serializer.data)
            # send to the api page (web browser)
            return HttpResponse(json_data, content_type='application/json')
        
        # sent all data from database when request is None.
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    

    # post method logic.
    if request.method == "POST":
        # data comes in json format convert into python format.
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        ser = StudentSerializer(data = python_data)
        if ser.is_valid():
            ser.save()
            # python form res
            res = {'msg':'Data created successfully..'}
            # convert into json.
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        # if error come when data is not validated.
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json')

    # put method logic (It is use to update pre-defined data.)
    if request.method == "PUT":
        json_data = request.body   # data comes in json form
        stream = io.BytesIO(json_data)   # convert json data into byte form
        python_data = JSONParser().parse(stream)  # convert into byte data into python.

        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        # serializer = StudentSerializer(stu, data=python_data) :- convert whole data into complex data
        serializer = StudentSerializer(stu, data=python_data, partial=True) # convert partial python data into complex data.
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated successfully.'}
            json_data = JSONRenderer().render(res)  # convert python data into json.
            return HttpResponse(json_data, content_type='application/json')  # send to the data to the thirdparty app in form of json.
        
        json_data = JSONRenderer().render(serializer.errors)  # convert python data into json.
        return HttpResponse(json_data, content_type='application/json')  # send to the data to the thirdparty app in form of json.
    

    # delete data logic.
    if request.method == 'DELETE':
        json_data = request.body   # jsondata fetch from request
        stream = io.BytesIO(json_data)   # jsondata convert into stream (means byte code)
        python_data = JSONParser().parse(stream)  # byte convert into python data.
        id = python_data.get('id')  # fetch id
        stu = Student.objects.get(id=id)  # fetch particular object through id.
        stu.delete()  # delete data
        res = {'msg':'Data Delete Successfully.'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    
    


