from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from .models import Departments,Questionnaire,Register,Responses
from .serializers import DepartmentSerializer,QuestionnaireSerializer,RegisterSerializer,ResponsesSerializer

from django.core.files.storage import default_storage

# Create your views here.
'''
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        #return JsonResponse(department_data,safe=False)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)
'''
@csrf_exempt
def get_sectors(request,id=0):
    if request.method=='GET':
        departments=Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    return invalid_method()
    
    
@csrf_exempt
def get_questions(request,id=0):
    if request.method=='GET':
        dept_id=JSONParser().parse(request)
        questionnaire=Questionnaire.objects.filter(department_id=dept_id["department_id"])
        questionnaire_serializer=QuestionnaireSerializer(questionnaire,many=True)
        return JsonResponse(questionnaire_serializer.data,safe=False)
    return invalid_method()
    

@csrf_exempt
def add_user_question(request,id=0):
    if request.method=='POST':
        questionnaire_data=JSONParser().parse(request)
        #return JsonResponse(questionnaire_data,safe=False)
        questionnaire_serializer=QuestionnaireSerializer(data=questionnaire_data)
        if questionnaire_serializer.is_valid():
            questionnaire_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed To Add",safe=False)        
    return invalid_method()

@csrf_exempt
def add_user_sector(request,id=0):
    if request.method=='POST':
        department_data=JSONParser().parse(request)
        #return JsonResponse(questionnaire_data,safe=False)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed To Add",safe=False)
    return invalid_method()
    
    
@csrf_exempt
def register(request,id=0):
    if request.method=='POST':
        register_data=JSONParser().parse(request)
        #return JsonResponse(register_data,safe=False)
        register_serializer=RegisterSerializer(data=register_data)
        if register_serializer.is_valid():
            register_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed To Add",safe=False)
    return invalid_method()
    
    
    
@csrf_exempt
def login(request,id=0):
    if request.method=='POST':
        login_data=JSONParser().parse(request)
        #return JsonResponse(register_data,safe=False)
        login_user=Register.objects.filter(phone_no=login_data["phone_no"]).filter(password=login_data["password"])
        
        login_serializer=RegisterSerializer(login_user,many=True)       
        if login_serializer.data:
            return JsonResponse(login_serializer.data,safe=False)
        return JsonResponse("Incorrect Phone / Passoword",safe=False)
    return invalid_method()
     
def invalid_method():
    return JsonResponse(data="Invalid Method",status=400,safe=False)   


        
@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)