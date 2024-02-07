from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'title': 'Главная страница'}
    def handle_uploaded_file(f):
        with open(f"uploads/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file_upload'])
        data = {'title': 'Главная страница'}
        return render(request, 'main/analitics.html', data)            
    
    return render(request, 'main/index.html', data)
    # return HttpResponse("Страница приложения women.")

