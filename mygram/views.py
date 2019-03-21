from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect

from .forms import NewPostForm, NewCommentForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment
from django.contrib.auth import authenticate, login 


@login_required(login_url='/accounts/login/')
def home(request):
     title='Home | MyGram'
     posts=Image.objects.all()
     return render(request,'grams/home.html',{'title':title , 'posts':posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.likes=0
            
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def post(request,id):
    post=Image.objects.get(id=id)
    comments=Comment.objects.filter(image=post)
    return render(request, 'grams/post.html', {"post": post, 'comments':comments})

@login_required(login_url='/accounts/login/')
def like_home(request,id):
     post=Image.objects.get(id=id)
     post.likes+=1
     post.save()
     return redirect('home')

@login_required(login_url='/accounts/login/')
def like_post(request,id):
     post=Image.objects.get(id=id)
     post.likes+=1
     post.save()
     return redirect('post',id=id)

@login_required(login_url='/accounts/login/')
def add_comment(request,id):
        current_user = request.user
        post=Image.objects.get(id=id)
        if request.method == 'POST':
               form = NewCommentForm(request.POST)
               if form.is_valid():
                    comment= form.cleaned_data['comment']
                   
                    new_comment = comment(comment = comment,user =current_user,image=image)
                    new_comment.save()
                    
                    HttpResponseRedirect('home')
               else:
                    form = NewCommentForm()
               return render(request, 'grams/new_comment.html', {"letterForm":form})

     # Create your views here.
