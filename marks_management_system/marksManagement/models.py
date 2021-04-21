from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=8 , unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.roll_no

class Faculty(models.Model):
    fId = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=30)
    subjectName = models.CharField(max_length=50)
    subjectCode = models.CharField(max_length=20)

class Subject(models.Model):
    rollNo =models.CharField(max_length=8 , unique=False)
    subjectCode = models.CharField(max_length=20 , unique=False)
    assignment1 = models.FloatField(default=0.00)
    assignment2 = models.FloatField(default=0.00)
    classtest1= models.FloatField(default=0.00)
    classtest2 = models.FloatField(default=0.00)
    midTerm =models.FloatField(default=0.00)
    endTerm = models.FloatField(default=0.00)
    

