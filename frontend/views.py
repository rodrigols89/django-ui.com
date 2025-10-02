from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')

def spacing(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/spacing.html')

def sizing(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/sizing.html')

def layout(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/layout.html')

def typography(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/typography.html')

def borders(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/borders.html')

def core_concepts(request):
    if request.method == 'GET':
        return render(request, 'pages/tailwind/core-concepts.html')
