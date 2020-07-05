from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
from django.conf import settings
from django.conf.urls.static import static
from .models import Feed
from django.shortcuts import redirect
import os
from chatbot.settings import BASE_DIR
file_path=os.path.join(BASE_DIR,'chatbot/chatbotcode2.py')

def feedback(request) :
    if request.method == 'POST':
        if request.POST["name_f"] and request.POST["email_f"] and request.POST["contact_f"] and request.POST["comment_f"]:
            feed=Feed()
            feed.name_f = request.POST['name_f']
            feed.email_f = request.POST['email_f']
            feed.contact_f = request.POST['contact_f']
            feed.comment_f = request.POST['comment_f']
            feed.save()
            #return redirect("http://127.0.0.1:8000/")
            return render(request, 'feedback.html',{'error':'thank you for you feedback'})
        else:
            return render(request, 'feedback.html',{'error':'some fields are empty, please fill all of them'})
    else :
         return render(request, 'feedback.html')

n1=[]
n2=[]
lp=-1

def home(request):
    return render(request,"home.html")

def first_page(request) :
    return render(request, 'first_page.html')

def contactus(request) :
    return render(request, 'contactus.html')

def info(request) :
    return render(request, 'info.html')

def chat(request) :
    global lp,n1,n2,name
    if lp==(-1):
        name = request.GET['name']
    inp=request.POST.get("box")
    if inp==None:
        n2.append("NULL")
        inp="hii "+name+" i'm chatbot, ready to answer your query. type your question in the box given below"
        n2.append(inp)
        lp+=1
        return render(request,"chat.html",{'name':name,'ans':n2,'question':n1})
    else:
        n2.append(inp)
        out=run([sys.executable,file_path,inp],shell=False,stdout=PIPE)
        r=out.stdout
        o=r.decode("utf-8")
        n2.append(o)
        lp+=1
        return render(request,"chat.html",{'name':name,'ans':n2,'question':n1})
