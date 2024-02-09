from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'title': 'Главная страница'}            
    
    return render(request, 'main/index.html', data)
    # return HttpResponse("Страница приложения women.")

