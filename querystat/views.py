#-*- coding: UTF-8 -*- 
import MySQLdb
from querystat.models import Pstat
from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import time

# Create your views here.

def getPstat(request):
    if request.user.is_authenticated():  
        sqlstr='SELECT id,trx_id,trx_mysql_thread_id,user,host,dhost,db,command,time,state,info,trx_stat,trx_wait_started,trx_query,blocking_trx_id,is_blocker,create_time FROM querystat_pstat order by create_time desc limit 10' 
        names = Pstat.objects.raw(sqlstr)
        hostList = Pstat.objects.all().values('dhost').distinct()
        return render_to_response('querystat.html', {'names': names,'hostList' : hostList},context_instance=RequestContext(request))
    else:
        response = HttpResponseRedirect('/login/')
        return response

def login(request):
    return render_to_response('login.html',context_instance=RequestContext(request))
   
def validateUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            response = HttpResponseRedirect('/pstat/')
        else:
            response = HttpResponseRedirect('/login/')
            
    else:
        return render_to_response('login.html',{'message' : '用户名或者密码错误!'},context_instance=RequestContext(request))

    return response

def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/login/')
    return response



def filterPstat(request):
    if 'start_form_time' in request.POST:
        stime = request.POST['start_form_time']
    else:
        stime = None 

    if 'end_form_time' in request.POST:
        etime  = request.POST['end_form_time']
    else:
        etime = None
   
    if 'host' in request.POST:
        host  = request.POST['host']
    else:
        host = None 
    
    if host is not None:
        request.session['host'] = host    


    if stime is not None:
        if etime is not None:
            request.session['stime'] = stime
            request.session['etime'] = etime
    if request.user.is_authenticated():
        if host is None:
            host=request.session.get('host')
        if stime is None:
            if etime is None:
                stime=request.session.get('stime')
                etime=request.session.get('etime')
        if stime == '':
            if etime == '':
                stime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-86400))
                etime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        hostList = Pstat.objects.all().values('dhost').distinct()
        if host == '':
            result = Pstat.objects.filter(create_time__gte=str(stime)).filter(create_time__lte=str(etime)).order_by('-create_time')
        else:
            result = Pstat.objects.filter(create_time__gte=str(stime)).filter(create_time__lte=str(etime)).filter(dhost=host).order_by('-create_time')
        paginator = Paginator(result , 10)
        page = request.GET.get('page')
        try:
            qstat = paginator.page(page)
        except PageNotAnInteger:
            qstat = paginator.page(1)
        except EmptyPage:
            qstat = paginator.page(paginator.num_pages)
        return render_to_response('filterpstat.html', {"qstat": qstat,"hostList" : hostList},context_instance=RequestContext(request))
    else:
        response = HttpResponseRedirect('/login/')
        return response
