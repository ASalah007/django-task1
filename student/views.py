import json

from django.http import Http404, JsonResponse
from django.shortcuts import HttpResponse, render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers


from .models import Student

class StudentListView(View):

    def get(self, req):
        all_students = Student.objects.all()
        all_students_json = serializers.serialize("json", all_students)
        return JsonResponse(json.loads(str(all_students_json)), safe=False)
        

class StudentEditView(View):

    def get(self, req, id):
        try:
            student = Student.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse("<h1> object doesn't exist </h1>")

        student_json = serializers.serialize("json", [student])
        return JsonResponse(json.loads(student_json)[0]["fields"], safe=False)
        

    def delete(self, req, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
        except ObjectDoesNotExist:
            return HttpResponse("<h1> object doesn't exist </h1>")

        return HttpResponse("<h1>Deleted</h1>")

    def put(self, req, id):
        s = json.loads(req.body.decode('UTF-8'))
        Student.objects.create(first_name=s["first_name"],
                               age=int(s["age"]),
                               class_room=s["class_room"], 
                               last_name=s["last_name"],
                               email=s["email"]
                               )
        return HttpResponse("new student added")

    def post(self, req, id):
        try:
            student = Student.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse("<h1> object doesn't exist </h1>")

        newstudent = json.loads(req.body.decode('UTF-8'))
        student.first_name = newstudent["first_name"];
        student.last_name = newstudent["last_name"];
        student.age = newstudent["age"];
        student.class_room = newstudent["class_room"];
        student.email = newstudent["email"];

        student.save()
        return HttpResponse("<h1>Updated</h1>")

