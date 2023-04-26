from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    tf=Topicform()
    d={'tf':tf}
    if request.method=='POST':
        tfd=Topicform(request.POST)
        if tfd.is_valid():
            topic_name=tfd.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=topic_name) [0]
            to.save()
            
            tqf=Topic.objects.all()
            d1={'tqf':tqf}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    wf=Webpageform()
    d={'wf':wf}
    if request.method=='POST':
        wfd=Webpageform(request.POST)
        if wfd.is_valid():
            topic_name=wfd.cleaned_data['topic_name']
            name=wfd.cleaned_data['name']
            url=wfd.cleaned_data['url']
            to=Topic.objects.get_or_create(topic_name=topic_name) [0]
            to.save()
            wo=Webpage.objects.get_or_create(topic_name=to,name=name,url=url) [0]
            wo.save()

            wqf=Webpage.objects.all()
            d1={'wqf':wqf}
            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    af=AccessRecordform()
    d={'af':af}
    if request.method=='POST':
        afd=AccessRecordform(request.POST)
        if afd.is_valid():
            name=afd.cleaned_data['name']
            author=afd.cleaned_data['author']
            date=afd.cleaned_data['date']
            wo=Webpage.objects.get(name=name)
            wo.save()
            ar=AccessRecord.objects.get_or_create(name=wo,author=author,date=date) [0]
            ar.save()

            aqf=AccessRecord.objects.all()
            d1={'aqf':aqf}
            return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)