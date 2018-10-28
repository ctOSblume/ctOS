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

def hacked(request):
    return render(request, 'chat/hacked.html', {})

def admini(request):
    return render(request, 'chat/admini.html', {})




def id6957(request):
    return render(request, 'chat/id6957.html', {})
def id9750(request):
    return render(request, 'chat/id9750.html', {})
def id0085(request):
    return render(request, 'chat/id0085.html', {})
def id0024(request):
    return render(request, 'chat/id0024.html', {})
def id2303(request):
    return render(request, 'chat/id2303.html', {})
def id9395(request):
    return render(request, 'chat/id9395.html', {})
def id5572(request):
    return render(request, 'chat/id5572.html', {})
def id3998(request):
    return render(request, 'chat/id3998.html', {})
def id1338(request):
    return render(request, 'chat/id1338.html', {})
def id7557(request):
    return render(request, 'chat/id7557.html', {})
def id4575(request):
    return render(request, 'chat/id4575.html', {})
def id7540(request):
    return render(request, 'chat/id7540.html', {})
def id7939(request):
    return render(request, 'chat/id7939.html', {})
def id5886(request):
    return render(request, 'chat/id5886.html', {})
def id1124(request):
    return render(request, 'chat/id1124.html', {})
def id5452(request):
    return render(request, 'chat/id5452.html', {})
def id8794(request):
    return render(request, 'chat/id8794.html', {})
def id0787(request):
    return render(request, 'chat/id0787.html', {})
