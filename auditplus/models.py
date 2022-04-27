from django.db import models
import datetime


class Departments(models.Model):
    dept_id=models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=45)
    
class Questionnaire(models.Model):
    question_id=models.AutoField(primary_key=True)
    question_description=models.TextField()
    department_id=models.IntegerField()
    industry=models.CharField(max_length=40)
    
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=100)
    email_id=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    
    
    
class Responses(models.Model):
    response_id=models.AutoField(primary_key=True)
    hospital=models.CharField(max_length=45)
    audit_no=models.IntegerField()
    comments=models.TextField()
    uploads=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    date=models.DateField(default=datetime.datetime.now().strftime("%x"))
    response_file= models.FileField(upload_to=None, max_length=254)
    dept=models.CharField(max_length=200)
    
    
class UserQuestionnaire(models.Model):
    user_id=models.IntegerField()
    question_id=models.AutoField(primary_key=True)
    question_description=models.TextField()
    department_id=models.IntegerField()
    industry=models.CharField(max_length=40)
    