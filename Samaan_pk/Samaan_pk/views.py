from django.shortcuts import render

def homepage(request):
    print("HOMEPAGE")
    return render(request, 'homepage.html')
