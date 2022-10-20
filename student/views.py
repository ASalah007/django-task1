from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
import json
import os


def list(request):
    path = os.path.join(os.getcwd(), "student/db.json")
    with open(path) as fp:
        data = json.load(fp)
    return JsonResponse(data, safe=False)

def update_delete(req, id):
    path = os.path.join(os.getcwd(), "student/db.json")

    if req.method == "POST":
        with open(path, "r+") as fp:
            data = json.load(fp)
            for i, obj in enumerate(data):
                if obj["id"] == id:
                    del data[i]
                    fp.truncate(0)
                    fp.seek(0)
                    json.dump(data, fp)
                    return HttpResponse("<h1>Deleted</h1>")
        return HttpResponse("<h1>not found</h1>")

    elif req.method == "PUT":
        with open(path, "r+") as fp:
            data = json.load(fp)
            new_obj = json.loads(req.body)
            for i, obj in enumerate(data):
                if obj["id"] == id:
                    data[i] = new_obj
                    fp.truncate(0)
                    fp.seek(0)
                    json.dump(data, fp)
                    return HttpResponse("<h1>Updated</h1>")
        return HttpResponse("<h1>not found</h1>")
        

    return HttpResponse("nothing is here")


