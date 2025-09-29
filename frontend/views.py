from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')

def spacing(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/spacing.html')
