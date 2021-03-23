from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Course,Branch,Register,MFY,Course_Part,Teacher,ManagerNITS,Skills
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import datetime
import time
import json

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def course(request):
    return render(request,'course.html')

def contact(request):
    return render(request,'contact.html')



def check_user(request):
        if request.method == 'GET':
          un = request.GET['usern']
          check = User.objects.filter(username=un)
          if len(check) == 1:
            return HttpResponse('Exists')
          else:
            return HttpResponse('No exists')



def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            else:
                res = HttpResponseRedirect('/')
                if 'rememberme' in request.POST:
                    res.set_cookie('user__id', user.id)
                    res.set_cookie('date_login', datetime.datetime.now())
                return res

        else:
            return render(request, 'index.html', {'status': 'Foydaluvchi nomi yoki paroli xato'})

    return HttpResponse('called')

@login_required
def manager(request):
    
    manager_branch=ManagerNITS.objects.filter(user=request.user.id)
    teacher=Teacher.objects.filter(Branch=ManagerNITS.objects.get(user=request.user.id).branch_id)

    course=Course.objects.all()
    mfy=MFY.objects.filter(branch=ManagerNITS.objects.get(user=request.user.id).branch_id)
    print(mfy)
    context={'course':course,'data':manager_branch,'teacher':teacher,'mfy':mfy}
    country_cod = '+998'
    if request.method=='POST':
        fname=request.POST['fname']#w
        lname=request.POST['lname']#w
        sname=request.POST['sname']#w
        passport=request.POST['passport']#w
        cnumber=request.POST['phone']#w
        bdate=request.POST['bdate']#w
        gender=request.POST['gender']#w
        branch=request.POST['branch']#w
        mfy=request.POST['mfy']#w
        course=request.POST['course']#w
        teacher=request.POST['teacher']
        group=request.POST['group']
        payment=request.POST['tolov']
        social_statement=request.POST['social_statement']
        sdate=request.POST['sdate']
        enddate=request.POST['enddate']
        subject=request.POST['subject']
        mobnumber = country_cod + cnumber
        usr=User.objects.create_user(passport,password=cnumber)
        usr.username=passport
        usr.first_name=fname
        usr.last_name=lname
        usr.save()
        reg=Register(user=usr,contact_number=mobnumber,branch = Branch.objects.get(id=branch),
        course=Course.objects.get(id=course),number_group=group,gender=gender,surname=sname,birth_date=bdate,
        mfy=MFY.objects.get(id=mfy),teacher=Teacher.objects.get(id=teacher),tolov=payment,social_state=social_statement,startdate=sdate,enddate=enddate,subject=subject)
        reg.save()
        return render(request, 'manager-panel.html',
                      {'status': 'Tabriklaymiz! Hurmatli , {} Siz ro`yxatdan muvaffaqiyatli o`tdingiz'.format(fname)})
    return render(request,'manager-panel.html',context)

def getteacher(request):
    if request.method=='POST':
        coursera= request.POST.get('coursera')
        skills=Skills.objects.filter(course_id=coursera)

    teacher=Teacher.objects.filter(Branch=ManagerNITS.objects.get(user=request.user.id).branch_id)
    regTeachId = []
    for i in teacher:
        regTeachId.append(i.fullname)

    skills_teacher=[]

    for i in skills:
        if i.teacher.fullname in regTeachId:
            
            skills_teacher.append({'name': i.teacher.fullname, 'id': i.teacher_id})
          
    # print(skills_teacher[1]['name'], skills_teacher[1]['id'])
    return HttpResponse(json.dumps({"skills": skills_teacher}), content_type="application/json")



@login_required
def user_logout(request):
    logout(request)
    res = HttpResponseRedirect('/')
    res.delete_cookie('user_id')
    res.delete_cookie('date_login')
    return res
def livechat(request):
    return render(request,'livechat.html')


def student(request):
    return render(request,'student.html')













def register(request):
    country_cod = '+998'
    course=Course.objects.all()
    branch=Branch.objects.all()
    context={'data':course,'branch':branch}
    if request.method=='POST':
        fname=request.POST['fname']#w
        lname=request.POST['lname']#w
        sname=request.POST['sname']#w
        username=request.POST['uname']#w
        email=request.POST['email']#w
        password1=request.POST['password1']#w
        cnumber=request.POST['cnumber']#w
        branch=request.POST['branch']#w
        course=request.POST['course']#w
        course_days=request.POST['edate']#w
        course_time_type=request.POST['cdate']#w
        mobnumber = country_cod + cnumber
        fullname=lname+' '+sname

        usr=User.objects.create_user(username,email,password1)
        usr.username=username
        usr.first_name=fname
        usr.last_name=fullname
        usr.save()
        reg=Register(user=usr,contact_number=mobnumber,branch = Branch.objects.get(id=branch),
        course=Course.objects.get(id=course),course_days=course_days,course_time_type=course_time_type,
        number_group=Course_Part.objects.get(id=1))
        reg.save()
        return render(request, 'register.html',
                      {'status': 'Tabriklaymiz! Hurmatli , {} Siz ro`yxatdan muvaffaqiyatli o`tdingiz'.format(fullname)})
    return render(request,'register.html',context)

def error_404_view(request,exception):
    return render(request,'404.html')
