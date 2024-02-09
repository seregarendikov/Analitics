from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def analytics(request):
    data = {'title': 'Аналитика'}
    def handle_uploaded_file(f):
        with open(f"uploads/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    if request.method == "POST":
        handle_uploaded_file(request.FILES['file_upload'])
        data = {'title': 'Аналитика'}
        return render(request, 'analytics/list_analitics.html', data)            
    
    return render(request, 'analytics/analytics.html', data)
    # return HttpResponse("Страница приложения women.")



