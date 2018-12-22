from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
#业务处理逻辑



    #request.POST
    #request.GET

    #return HttpResponse("hello word")

templist=[
    {"user":"jack","pwd":"asd"},
    {"user": "ba", "pwd": "a123"},
]
def index(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username,pwd=password)
        user_list=models.UserInfo.objects.all()
        print(user_list)

        temp={"user":username,"pwd":password}
        templist.append(temp)
    elif request.method=="GET":
        return render(request,"index.html")

    return render(request,"index.html",{"data":user_list})
