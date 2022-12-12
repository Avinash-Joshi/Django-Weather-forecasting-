from django.shortcuts import render
from django.http import HttpResponse
from .models import Data,Contact

# Create your views here.


def index(request):
    posts = Data.objects.all()
    print("Post: ",posts)
    # print(len(posts))
    length=len(posts)
    location=request.GET.get('Currentstate','default')
    location=location.upper()
    print(location)  
    print(type(location))
    # print(posts)  
    if(location!=" " and location!="" and location!='default'): 
    # print(posts.State_id)   
        inner=Data.objects.values('State').all()
        print(inner)
        values= Data.objects.all().values()
        print(values)
        for i in range(length):
            print(i)
            print(values[i]['State'])
        dic1={}
        j=-1
        for i in range(length):
            if (values[i]['State']==location):
                dic1=values[i]
                # print(dic1)
                j=i
        print("Value is ",dic1) 
        dic=[(k,v) for k,v in dic1.items()]
        print(dic)
        # print("Hello")
        if(j!=-1):
            state=values[j]['State'].capitalize()
            Temp=values[j]['Today_Temp']
            wind=values[j]['Today_wind']
            condition=values[j]['Today_condition']
            # sunrise=values[j]['Today_sunrise']
            # sunset=values[j]['Today_sunset']
            TvD_plot=values[j]['TempVsDate']
            CvD_plot=values[j]['ConditionVsDate']
            param={'dic':dic1,'state':state,'temp':Temp,'wind':wind,'condition':condition,'Tempplot':TvD_plot,'Condplot':CvD_plot}
            # state="MP"
            # Temp=19
            # param={'dic':dic1,'state':state,'temp':Temp}
            # param={'state':state,'temp':Temp,'wind':wind,'condition':condition,'Tempplot':TvD_plot}
            return render(request,"weather/Result.html",param)
        if(request.method=='POST'):
            name=request.POST.get('Name','default')
            phone=request.POST.get('Phone','default')
            email=request.POST.get('Email','default')
            issue=request.POST.get('Issue','default')
    
            print(name)
            print(phone)
            print(email)
            print(issue)
    
            if(issue!=""):
                contact=Contact(Name=name,Phone=phone,Email=email,Issue_or_Feedback=issue)
                contact.save()
                if name!='default' or name!='':
                    return render(request,'weather/index.html')
        return render(request,"weather/index.html")



    if(request.method=='POST'):
        name=request.POST.get('Name','default')
        phone=request.POST.get('Phone','default')
        email=request.POST.get('Email','default')
        issue=request.POST.get('Issue','default')

        print(name)
        print(phone)
        print(email)
        print(issue)

        if(issue!=""):
            contact=Contact(Name=name,Phone=phone,Email=email,Issue_or_Feedback=issue)
            contact.save()
            if name!='default' or name!='':
                return render(request,'weather/index.html')
    return render(request,"weather/index.html")


def help(request):
    return render(request,'weather/help.html')    