from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .form import form_user, form_user_article
from .models import model_user_article, model_like_article
from django import forms
from django.http import HttpResponse
import datetime
# Create your views here.



def time_date(temp):
    time = str(datetime.datetime.now().date())[0:10]
    temp = str(temp)[0:10]
    if time[0:4] != temp[0:4]:
        val = int(int(time[0:4])-int(temp[0:4]))
        if val == 1: return "a year ago"
        else: return (str( int(time[0:4])-int(time[0:4]) )+" Years ago")
        # print(str(int(time[0:4])-int(time[0:4]))," year ago")
    elif time[5:7] != temp[5:7]:
        val = int( int(time[5:7])-int(temp[5:7]))
        # date.append( str ( int(time[5:7])-int(time[5:7])))
        if val == 1: return  "a Month ago"
        else: return (str( int(time[0:4])-int(time[0:4]) )+" Months ago")
        # print(str(int(time[0:4])-int(time[0:4]))," month ago")
    else :
        # date.append(str(int(time[8:])-int(time[8:])))
        val = int( int(time[8:])-int(temp[8:]) )
        if val == 0: return "Today"#article_veiw.date = "Today"
        elif val == 1: return "Yesterday" #article_veiw.date = "Yesterday"
        else: return (str( int(time[8:])-int(temp[8:]) )+"  days ago")



# @login_required
def index(request):
    articles = model_user_article.objects.all()
    for article in articles:
        article.date = time_date(article.date)
        article.content =article.content[0:210]
    return render(request,'accounts/index.html',{'articles':articles })

def registration(request):
    register=False
    if request.method == 'POST':
        user_input = form_user(data=request.POST)
        if user_input.is_valid():
            user = user_input.save()
            temp=user_input.cleaned_data['email']
            user.username = temp
            user.set_password(user.password)
            user.save()
            return render(request,'accounts/index.html')
        else:
            print(user_input.errors)
            print(article_input.errors)
    user_form = form_user
    print("m registarrti mhu ")
    return render(request, 'accounts/registration.html',{'user_form': user_form})


@login_required
def user_article(request):
    articles = model_user_article.objects.all().filter(user=request.user)
    for article in articles:
        article.date = time_date(article.date)
        article.content =article.content[0:210]
    return render(request,'accounts/user_article.html',{'articles':articles })

@login_required
def add_article(request):
    if request.method == 'POST':
        user_input = form_user_article(data=request.POST)
        if user_input.is_valid():
            article = user_input.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('user_article')
        else:
            print(user_input.errors)
    user_form = form_user_article
    print("m registarrti mhu ")
    return render(request,'accounts/add_article.html',{'user_form': user_form})

#change
def article(request, ide):
    article_veiw =  model_user_article.objects.get(header=ide)
    article_veiw.likes = article_veiw.likes+1
    article_veiw.save()
    articles = model_user_article.objects.all()
    for article in articles:
        article.date = time_date(article.date)
        article.content =article.content[0:210]
    article_veiw.date = time_date(article_veiw.date)
    return render(request,'accounts/article.html', {'article':article_veiw,'article_all':articles })
