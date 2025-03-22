from django.shortcuts import render



def index(request):
    context = {
        'title': 'Home Page',
        'content': 'Welcome to the home page!',
    }

    return render(request, 'app_main/index.html', context)



