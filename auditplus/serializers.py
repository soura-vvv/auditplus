from rest_framework import serializers
from .models import Departments,Questionnaire,Register,Responses

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('dept_id','dept_name')
        
class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questionnaire
        fields=('question_id','question_description','department_id','industry')
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=('id','firstname','lastname','username','password','cpassword','phone_no','card_no','time')


class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Responses
        fields=('response_id','hospital','audit_no','comments','uploads','date','response_file','dept')        
        
        
   