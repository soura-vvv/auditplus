from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from .models import Departments,Questionnaire,Register,Responses,UserQuestionnaire,UserSectors
from .serializers import DepartmentSerializer, QuestionnaireSerializer,RegisterSerializer,ResponsesSerializer,UserQuestionnaireSerializer,UserSectorsSerializer

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
        response_data = {}
        response_data['message'] = 'Success'
        response_data['data'] = departments_serializer.data
        return JsonResponse(response_data,status=200,safe=False)
    return invalid_method()
    
    
@csrf_exempt
def get_questions(request,id=0):
    if request.method=='POST':
        dept_id=JSONParser().parse(request)
        questionnaire=Questionnaire.objects.filter(department_id=dept_id["department_id"])
        questionnaire_serializer=QuestionnaireSerializer(questionnaire,many=True)
        if questionnaire_serializer.data:
            response_data = {}
            response_data['message'] = 'Success'
            response_data['data'] = questionnaire_serializer.data
            return JsonResponse(response_data,status=200,safe=False)
        return JsonResponse({'message' : 'Department not found.'},status=404,safe=False)
    return invalid_method()
    

@csrf_exempt
def add_user_question(request,id=0):
    if request.method=='POST':
        user_questionnaire_data=JSONParser().parse(request)
        #return JsonResponse(questionnaire_data,safe=False)
        user_questionnaire_serializer=UserQuestionnaireSerializer(data=user_questionnaire_data)
        if user_questionnaire_serializer.is_valid():
            user_questionnaire_serializer.save()
            return JsonResponse({'message' : 'Added successsfully.'}, status=200,safe=False)
        return JsonResponse({'message' : 'Failed to add.'},status=500,safe=False)        
    return invalid_method()

@csrf_exempt
def add_user_sector(request,id=0):
    if request.method=='POST':
        user_sector_data=JSONParser().parse(request)
        #return JsonResponse(questionnaire_data,safe=False)
        user_sector_serializer=UserSectorsSerializer(data=user_sector_data)
        if user_sector_serializer.is_valid():
            user_sector_serializer.save()
            return JsonResponse({'message' : 'Added successsfully.'},status=200,safe=False)
        return JsonResponse({'message' : 'Failed to add.'},status=500,safe=False)
    return invalid_method()
    
@csrf_exempt
def get_user_questions(request,id=0):
    if request.method=='GET':
        user_data=JSONParser().parse(request)
        user_questions=UserQuestionnaire.objects.filter(user_id=user_data["user_id"]).filter(department_id=user_data["department_id"])
        #return JsonResponse(questionnaire_data,safe=False)
        user_questionnaire_serializer=UserQuestionnaireSerializer(user_questions,many=True)
        if user_questionnaire_serializer.data:
            response_data={}
            response_data['message']='Success'
            response_data['data']={'topic_id':user_questionnaire_serializer.data[0]['topic_id'],'question_description':user_questionnaire_serializer.data[0]['question_description'],}
            return JsonResponse(response_data,status=200,safe=False)
        return JsonResponse({'message' : 'Invalid.'},status=500,safe=False)
    return invalid_method() 
    
 
 
 
@csrf_exempt
def register(request,id=0):
    if request.method=='POST':
        register_data=JSONParser().parse(request)
        #return JsonResponse(register_data,safe=False)
        register_serializer=RegisterSerializer(data=register_data)
        if register_serializer.is_valid():
            register_serializer.save()
            response_data = {}
            response_data['message'] = 'Success'
            return JsonResponse(response_data,status=200,safe=False)
        return JsonResponse({'message' : 'Failed to add.'},status=500,safe=False)
    return invalid_method()
    
    
    
@csrf_exempt
def login(request,id=0):
    if request.method=='POST':
        login_data=JSONParser().parse(request)
        #return JsonResponse(register_data,safe=False)
        login_user=Register.objects.filter(phone_no=login_data["phone_no"]).filter(password=login_data["password"])
        
        login_serializer=RegisterSerializer(login_user,many=True)       
        if login_serializer.data:
            response_data = {}
            response_data['message'] = 'Success'
            response_data['data'] = {'id' : login_serializer.data[0]['id'] , 'firstname' : login_serializer.data[0]['firstname'] , 'lastname' : login_serializer.data[0]['lastname']}
            return JsonResponse(response_data,status=200,safe=False)
        return JsonResponse({'message' : 'Incorrect Phone / Password'},status=404,safe=False)
    return invalid_method()
     
def invalid_method():
    return JsonResponse(data="Invalid Method",status=400,safe=False)   


        
@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

