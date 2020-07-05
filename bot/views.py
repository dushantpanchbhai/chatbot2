from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
from django.conf import settings
from django.conf.urls.static import static

n1=[]
n2=[]
lp=-1
def home(request):
    return render(request,"home.html")

def ans(request):
    global lp,n1,n2
    inp=request.POST.get("box")
    n2.append(inp)
    out=run([sys.executable,"//home//dushant//Desktop//django//chatbot//chatbot//chatbot.py",inp],shell=False,stdout=PIPE)
    r=out.stdout
    o=r.decode("utf-8")
    n2.append(o)
    lp+=1
    return render(request,"ans.html",{'name':name,'ans':n2,'question':n1,'index':lp})

def first_page(request) :
    return render(request, 'first_page.html')


def feedback(request) :
    return render(request, 'feedback.html')

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
        inp="hii"
    n2.append(inp)
    out=run([sys.executable,"//home//dushant//Desktop//django//chatbot2//chatbot//chatbotcode2.py",inp],shell=False,stdout=PIPE)
    r=out.stdout
    o=r.decode("utf-8")
    n2.append(o)
    lp+=1
    return render(request,"chat.html",{'name':name,'ans':n2,'question':n1,'index':len(n1)})
