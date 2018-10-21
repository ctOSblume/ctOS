from django.shortcuts import render

def post_list(request):
    return render(request, 'chat/post_list.html', {})
