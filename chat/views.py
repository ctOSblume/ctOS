from django.shortcuts import render

def post_list(request):
    return render(request, 'chat/post_list.html', {})

def info(request):
    return render(request, 'chat/info.html', {})

def info_full(request):
    return render(request, 'chat/info_full.html', {})

def command_full(request):
    return render(request, 'chat/command_full.html', {})

def command(request):
    return render(request, 'chat/command.html', {})
