from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse
import sqlite3,os
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from news.models import News,Video,Main,Oper,Picshow
import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
#import logging
import json



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def wechat(req):
   newslist = News.objects.filter(ispublished = 1, wxread__gte = 200).order_by('wxread')[::-1]
   #newslist = News.objects.filter(wxsj__contains =  datetime.date.today() - datetime.timedelta(days = 1))
   operlist = Oper.objects.order_by('id')
   #data = Picshow.objects.order_by('id')
   #data = Picshow.objects.order_by('id')
   data = serializers.serialize("json", Picshow.objects.all())
   #data = json.dumps(Picshow.objects.all())
   #defaultpicdefaultpic = '/media/uploadImages/snc.jpg'
   defaultpic = Picshow.objects.get(id = '1')
   return render(req, 'wechat.html', {'list':newslist, 'operlist':operlist, 'picshowlist':data, "dpic":defaultpic})

def newslist(req):
   newslist = News.objects.filter(ispublished = 1, wxread__gte = 200).order_by('wxread')[::-1]
   #newslist = News.objects.filter(wxsj__contains =  datetime.date.today() - datetime.timedelta(days = 1))
   operlist = Oper.objects.order_by('id')
   #data = Picshow.objects.order_by('id')
   data = Picshow.objects.order_by('id')
   #data = serializers.serialize("json", Picshow.objects.all())
   #data = json.dumps(Picshow.objects.all())
   #defaultpicdefaultpic = '/media/uploadImages/snc.jpg'
   #defaultpic = Picshow.objects.get(id = '1')
   paginator = Paginator(newslist,8)
   page = req.GET.get('page')
   try:
      newslist = paginator.page(page)
   except PageNotAnInteger:
      newslist = paginator.page(1)
   except EmptyPage:
      newslist = paginator.page(paginator.num_pages)
   return render(req, 'newslist.html', {'list':newslist, 'operlist':operlist, 'picshowlist':data})

def videos(req):


   videoslist = Video.objects.all().order_by('id')[::-1]
   operlist = Oper.objects.order_by('id')
   paginator = Paginator(videoslist,3)
   page = req.GET.get('page')
   try:
      videoslist = paginator.page(page)
   except PageNotAnInteger:
      videoslist = paginator.page(1)
   except EmptyPage:
      videoslist = paginator.page(paginator.num_pages)
   return render(req, 'videos.html', {'list':videoslist, 'operlist':operlist})

def mp4list(req):


   mp4list = Video.objects.all().order_by('id')[::-1]
   operlist = Oper.objects.order_by('id')
   data = Picshow.objects.order_by('id')
   paginator = Paginator(mp4list,4)
   page = req.GET.get('page')
   try:
      mp4list = paginator.page(page)
   except PageNotAnInteger:
      mp4list = paginator.page(1)
   except EmptyPage:
      mp4list = paginator.page(paginator.num_pages)
   return render(req, 'mp4list.html', {'list':mp4list, 'operlist':operlist, 'picshowlist':data})

def mp4play(req, pk):


   video = get_object_or_404(Video,pk=pk)
   operlist = Oper.objects.order_by('id')
   return render(req, 'mp4play.html', {'avideo':video, 'operlist':operlist})

def main(req):
    mainlist = Main.objects.order_by('id')
    operlist = Oper.objects.order_by('id')
    data = serializers.serialize("json", Picshow.objects.all())
    #data = json.dumps(Picshow.objects.all())
    defaultpic = Picshow.objects.get(id = '1')
    #data = Picshow.objects.all()
    return render(req, 'main.html', {'list':mainlist, 'operlist':operlist, 'picshowlist':data, 'dpic':defaultpic})

def index(req):
    mainlist = Main.objects.order_by('id')
    operlist = Oper.objects.order_by('id')
    #data = serializers.serialize("json", Picshow.objects.all())
    #data = json.dumps(Picshow.objects.all())
    #data = Picshow.objects.exclude(id = '1')
    data = Picshow.objects.order_by('id')
    #defaultpic = Picshow.objects.get(id = '1')
    #data = Picshow.objects.all()
    
    return render(req, 'index.html', {'list':mainlist, 'operlist':operlist, 'picshowlist':data})

def apk_down_full(req):
    def file_iterator(file_name, chunk_size=512):  
        with open(file_name,'rb') as f:  
            while True:  
                c = f.read(chunk_size)  
                if c:  
                    yield c  
                else:  
                    break  
    the_file_name = os.path.join(BASE_DIR, "media/aqyjfull.apk")
    #the_file_name = 'D:\\caoqianming\\xx\\ctcnews\\media\\aqyjfull.apk'
    response = StreamingHttpResponse(file_iterator(the_file_name))  
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="aqyjfull.apk"'
    return response
    #return render(req, 'media/aqyjfull.apk')

def apk_down_simple(req):
    def file_iterator(file_name, chunk_size=512):  
        with open(file_name,'rb') as f:  
            while True:  
                c = f.read(chunk_size)  
                if c:  
                    yield c  
                else:  
                    break  
    the_file_name = os.path.join(BASE_DIR, "media/aqyjsimple.apk")
    #the_file_name = 'D:\\caoqianming\\xx\\ctcnews\\media\\aqyjsimple.apk'
    response = StreamingHttpResponse(file_iterator(the_file_name))  
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="aqyjsimple.apk"'
    return response
    #return render(req, 'media/aqyjsimple.apk')

def appdown(req):
   return render(req, 'appdown.html')

@csrf_exempt
def calzan(req):
    if req.method == 'POST':
        vid = int(req.POST.get('id'))
        vzan = int(req.POST.get('zan'))
        print(vid,vzan)
        rejson = {'zan': vzan}
        Video.objects.filter(id = vid).update(zan = vzan)
        return HttpResponse(json.dumps(rejson), content_type = 'application/json')
        
   
