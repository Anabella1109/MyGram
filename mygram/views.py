from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NewPostForm, NewCommentForm, Profileform
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, Follow, Likes
from django.contrib.auth import authenticate, login 
impor


@login_required(login_url='/accounts/register/')
def home(request):
     title='Home | MyGram'
     current_user=request.user
     profile=Profile.objects.get(user=current_user)
     following=Follow.objects.filter(follower=profile)
     posts=Image.objects.all()
    
     return render(request,'grams/home.html',{'title':title , 'posts':posts, 'following':following})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            likes=Likes(likes=0,liked=False,user=current_user)
            likes.save()
            post.likes=likes
            
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def post(request,id):
    post=Image.objects.get(id=id)
    number_of_likes = Likes.objects.filter(image=post).count()

    comments=Comment.objects.filter(image=post)
    return render(request, 'grams/post.html', {"post": post, 'comments':comments, 'likes':number_of_likes})

@login_required(login_url='/accounts/login/')
def like_home(request,picture_id):
    post=Image.objects.get(id=picture_id)
    new_like, created = Likes.objects.get_or_create(user=request.user, image_id=picture_id)
    number_of_likes = Likes.objects.filter(image=post).count()
    post.likess=number_of_likes
    post.save()
    if not created:
        message='U already liked the picture'
    else:
        message='like successful'
    return redirect('home')
@login_required(login_url='/accounts/login/')
def like_post(request, picture_id):
    post=Image.objects.get(id=picture_id)
    new_like, created = Likes.objects.get_or_create(user=request.user, image_id=picture_id)
    if not created:
        message='U already liked the picture'
    else:
        message='like successful'
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
     images=Image.objects.filter(user=user)
     following=Follow.objects.filter(follower=profile).distinct()
     followers=Follow.objects.filter(following=profile).distinct()
    
     return render(request, 'grams/profile.html',{"user":user,"profile": profile, 'images':images,'following':following,'followers':followers})
     
@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.user=current_user
            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})


@login_required(login_url='/accounts/login/')
def user_follow(request):
    user_id = request.POST.get('id', None)
    action = request.POST.get('action', '')

    FOLLOW_ACTION = 'follow'
    UNFOLLOW_ACTION = 'unfollow'

    if request.user.is_anonymous:
        return JsonResponse({
            'status':'ko',
            'message': 'You must login'}
        )

    if action not in [FOLLOW_ACTION, UNFOLLOW_ACTION]:
        return JsonResponse({
            'status':'ko',
            'message': 'Unknown action {}'.format(action)}
        )

    try:
        user = User.objects.get(id=user_id)
        if action == UNFOLLOW_ACTION:
            Contact.objects.filter(user_from=request.user,user_to=user).delete()
            return JsonResponse({
                'status':'ok'
                })
        else:
            contact, created = Contact.objects.get_or_create( user_from=request.user, user_to=user)
            return JsonResponse({
                'status':'ok',
                'message': 'Following id : {}'.format(contact.id)
            })
    return redirect('profile', id)

@login_required(login_url='/accounts/login/')
def followers(request,id):
     profile=Profile.objects.get(id=id)
     followers=Follow.objects.filter(following=profile).distinct()
     return render(request, 'followers.html', { 'followers':followers, 'profile':profile})

