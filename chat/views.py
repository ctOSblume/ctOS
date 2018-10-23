from django.shortcuts import render
from .models import Post
from django.utils import timezone

def chat(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chat/chat.html', {'posts': posts})

def ctOS(request):
    return render(request, 'chat/ctOS.html', {})

def info(request):
    return render(request, 'chat/info.html', {})

def info_full(request):
    return render(request, 'chat/info_full.html', {})

def command_full(request):
    return render(request, 'chat/command_full.html', {})

def command(request):
    return render(request, 'chat/command.html', {})