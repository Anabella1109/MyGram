from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NewPostForm, NewCommentForm, Profileform
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, Follow
from django.contrib.auth import authenticate, login 


@login_required(login_url='/accounts/register/')
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
     return redirect('post',post.id)

@login_required(login_url='/accounts/login/')
def add_comment(request,id):
        current_user = request.user
        post=Image.objects.get(id=id)
        if request.method == 'POST':
               form = NewCommentForm(request.POST)
               if form.is_valid():
                    comment= form.cleaned_data['comment']
                   
                    new_comment = Comment(comment = comment,user =current_user,image=post)
                    new_comment.save()
                    
                    HttpResponseRedirect('home')
        else:
                    form = NewCommentForm()
        return render(request, 'grams/new_comment.html', {"letterForm":form,'post':post,'user':current_user})
@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'grams/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'grams/search.html',{"message":message})

     

def search_by_username(name):
       users=User.objects.filter(username__icontains=name)
       return users
@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     images=Image.objects.filter(profile=profile)
     return render(request, 'grams/profile.html',{"user":user,"profile": profile, 'images':images})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
           
            
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})


@login_required(login_url='/accounts/login/')
def follow(request,id):
    current_user = request.user
    profile2=Profile.objects.get(user=current_user)
    profile1=Profile.objects.get(id=id)
    follow=Follow(follower=profile2,following=profile1)
    follow.save()
    return redirect('profile',profile2.id)
